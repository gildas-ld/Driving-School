SELECT PG_TERMINATE_BACKEND(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'drivingschool-gildas.le-drogoff'
  AND pid <> PG_BACKEND_PID();
DROP DATABASE IF EXISTS "drivingschool-gildas.le-drogoff";
CREATE DATABASE "drivingschool-gildas.le-drogoff" WITH OWNER wac;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
GRANT ALL ON SCHEMA public TO wac;