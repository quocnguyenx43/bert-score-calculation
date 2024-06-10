import pandas as pd
import numpy as np
import csv

import sqlite3
from itertools import combinations
import argparse as arg

import bert_score

from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")


parser = arg.ArgumentParser(description="Params")
parser.add_argument("--db_file_path", type=str)
parser.add_argument("--type", type=str)
parser.add_argument("--from_", type=int)
parser.add_argument("--to_", type=int)
args = parser.parse_args()
args = vars(args)


def extract_data(db_file_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path) # './historical_databases/database_trainee/40.db'
    cursor = conn.cursor()

    # Tables
    tables = ['annotation', 'recruitment']

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        with open(f'output_tables/{table}.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(data)
            
    conn.close()

print('file: ', args['db_file_path'])
print('type: ', args['type'])
print('from - to: ', args['from_'], "-", args['to_'])

extract_data(args['db_file_path'])
ann = pd.read_csv('output_tables/annotation.csv')
rcmt = pd.read_csv('output_tables/recruitment.csv')
rcmt = rcmt[['index', 'id']]
rcmt.columns = ['index', 'recruiment_id']
df = pd.merge(rcmt, ann, on='recruiment_id', how='right')
df = df[df.user_id != 1]

counts = df.user_id.value_counts().sort_index()
indexes = [2, 3, 4, 6, 7, 8, 9, 10, 11]
names = ['VQuoc', 'TDuong', 'BKhanh', 'QNhu', 'TDinh', 'HGiang', 'BHan', 'Kiet', 'HAnh']
index_to_name = dict(zip(indexes, names))
index_to_count = counts.to_dict()
df_counts = pd.DataFrame({'name': index_to_name, 'count': index_to_count})
df_counts = df_counts.set_index(df_counts.index)
df_counts['count'].fillna(0, inplace=True)
print(df_counts.T)

def fill_annotator(annos):
    index_to_name_reverse = {v: k for k, v in index_to_name.items()}
    re = [index_to_name_reverse[name] for name in annos]
    return df[df.user_id.map(lambda x: x in re)]

if args['type'] == 'full':
    df = fill_annotator(['VQuoc', 'TDuong', 'BKhanh', 'QNhu', 'TDinh', 'HGiang', 'BHan', 'Kiet', 'HAnh'])
else:
    df = fill_annotator(['VQuoc', 'TDuong', 'BKhanh'])
print('After filtering: ')
print(df.user_id.value_counts().T)

pv_table_expl = df.pivot(index='recruiment_id', columns='user_id', values='explanation')
pv_table_expl.columns = pv_table_expl.columns.map(index_to_name)
pv_table_expl.dropna(inplace=True)
pv_table_expl = pv_table_expl[args['from_']: args['to_']]
print('Len data: ' + str(len(pv_table_expl)))

def bert_score_each_sample(li_expl_sents):
    # li_expl_sents = sent_1, sent_2, sent_3,...
    precisions, recalls, f1s = [], [], []
    combinations_two = list(combinations(li_expl_sents, 2))
    for comb in combinations_two:
        precision, recall, f1 = bert_score.score(
            [comb[0]], [comb[1]],
            model_type='bert-base-multilingual-cased',
            lang='vi', 
            verbose=False,
            device='cuda',
            batch_size=32,
        )
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)

    return np.mean(precisions), np.mean(recalls), np.mean(f1s)

def bert_score_func(df):
    df = df.to_numpy()
    precisions, recalls, f1s = [], [], []
    with tqdm(df, desc=f"Hi") as df_loader:
        for i, sample in enumerate(df):
            df_loader.set_description(f"Hi, {i + 1}/{len(df)}")

            precision, recall, f1 = bert_score_each_sample(sample)
            precisions.append(precision)
            recalls.append(recall)
            f1s.append(f1)
    
    return np.mean(precisions), np.mean(recalls), np.mean(f1s)

prec, rec, f1 = bert_score_func(pv_table_expl)
print(f"From " + str(args['from_']) + " to " + str(args['to_']))
print(f'prec: {prec}, recall: {rec}, f1: {f1}')
print()
print()