#!/usr/bin/env sh

python -m venv venv;
source ./venv/bin/activate;
# Check if VIRTUAL_ENV is set
echo $VIRTUAL_ENV;

python -m pip install --upgrade pip setuptools wheel;
pip install -r ./requirements.txt;

cp .env.example .env;

python manage.py migrate && \
python manage.py loaddata ./drivingschool/fixtures/0000_all.json && \
rm -rfv staticfiles;
python manage.py collectstatic;
python manage.py runserver