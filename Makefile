# include .env
# export $(shell sed 's/=.*//' .env)

run:
	sh run.sh
reset-pg-db:
	PGPASSWORD="bob" psql -U postgres --host=127.0.0.1 --port=2345 -d "drivingschool-gildas.le-drogoff" -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public ; GRANT ALL ON SCHEMA public TO postgres ; GRANT ALL ON SCHEMA public TO public;"

