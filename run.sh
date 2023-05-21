#!/usr/bin/env sh

# if [ -f .env ]; then
#   export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
# fi
FIXTURES="./drivingschool/fixtures/*"

python -m venv venv;
source ./venv/bin/activate;
# Check if VIRTUAL_ENV is set
echo $VIRTUAL_ENV;

python -m pip install --upgrade pip setuptools wheel;
pip install -r ./requirements.txt;

cp .env.example .env;

# rm -rfv db.sqlite3;

python manage.py migrate && \
for f in $FIXTURES
do
  echo "Processing $f file..."
  python manage.py loaddata "$f"
  ls "$f"
done
rm -rfv staticfiles;
python manage.py collectstatic;
python manage.py runserver

# USER : gildas.le-drogoff@epitech.eu
# PWD  : MDPMDPMDP
