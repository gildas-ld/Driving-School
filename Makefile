# include .env
# export $(shell sed 's/=.*//' .env)

run: clean-database
	sh run.sh
	
reset-pg-db:
	PGPASSWORD="bob" psql -U postgres --host=127.0.0.1 --port=2345 -d "drivingschool-gildas.le-drogoff" -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public ; GRANT ALL ON SCHEMA public TO postgres ; GRANT ALL ON SCHEMA public TO public;"

clean-database:
	PGPASSWORD="bob" psql -U wac --host=127.0.0.1 --port=2345 \
	-d postgres -f './clean-database.sql';

lint:
	source ./venv/bin/activate && black .