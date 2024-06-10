
echo "======= GOLDEN ======="

echo "ROUND 1"

python run.py --db_file_path "./database_golden/1.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_golden/3.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_golden/4.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_golden/6.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_golden/7.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_golden/10.db" --type "golden" --from_ 0 --to_ 50

python run.py --db_file_path "./database_trainee/1.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/2.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/5.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/12.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/13.db" --type "golden" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/26.db" --type "golden" --from_ 0 --to_ 50

echo "ROUND 2"

python run.py --db_file_path "./database_golden/2.db" --type "golden" --from_ 50 --to_ 100
python run.py --db_file_path "./database_golden/3.db" --type "golden" --from_ 50 --to_ 100
python run.py --db_file_path "./database_golden/5.db" --type "golden" --from_ 50 --to_ 100
python run.py --db_file_path "./database_golden/6.db" --type "golden" --from_ 50 --to_ 100
python run.py --db_file_path "./database_golden/7.db" --type "golden" --from_ 50 --to_ 100

python run.py --db_file_path "./database_trainee/11.db" --type "golden" --from_ 50 --to_ 100
python run.py --db_file_path "./database_trainee/31.db" --type "golden" --from_ 50 --to_ 100

echo "ROUND 3"

python run.py --db_file_path "./database_golden/8.db" --type "golden" --from_ 100 --to_ 150
python run.py --db_file_path "./database_trainee/32.db" --type "golden" --from_ 100 --to_ 150
python run.py --db_file_path "./database_trainee/37.db" --type "golden" --from_ 100 --to_ 150

echo "ROUND 4"

python run.py --db_file_path "./database_golden/9.db" --type "golden" --from_ 150 --to_ 200
python run.py --db_file_path "./database_trainee/37.db" --type "golden" --from_ 150 --to_ 200

echo "ROUND 5"

python run.py --db_file_path "./database_trainee/39.db" --type "golden" --from_ 200 --to_ 250


echo "======= TRAINEE ======="

echo "ROUND 1"

python run.py --db_file_path "./database_trainee/2.db" --type "full" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/11.db" --type "full" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/12.db" --type "full" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/20.db" --type "full" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/29.db" --type "full" --from_ 0 --to_ 50
python run.py --db_file_path "./database_trainee/31.db" --type "full" --from_ 0 --to_ 50

echo "ROUND 2"

python run.py --db_file_path "./database_trainee/11.db" --type "full" --from_ 50 --to_ 100
python run.py --db_file_path "./database_trainee/25.db" --type "full" --from_ 50 --to_ 100
python run.py --db_file_path "./database_trainee/31.db" --type "full" --from_ 50 --to_ 100
python run.py --db_file_path "./database_trainee/37.db" --type "full" --from_ 50 --to_ 100

echo "ROUND 3"

python run.py --db_file_path "./database_trainee/32.db" --type "full" --from_ 100 --to_ 150
python run.py --db_file_path "./database_trainee/37.db" --type "full" --from_ 100 --to_ 150

echo "ROUND 4"

python run.py --db_file_path "./database_trainee/37.db" --type "full" --from_ 150 --to_ 200
python run.py --db_file_path "./database_trainee/38.db" --type "full" --from_ 150 --to_ 200

echo "ROUND 5"

python run.py --db_file_path "./database_trainee/40.db" --type "full" --from_ 200 --to_ 250