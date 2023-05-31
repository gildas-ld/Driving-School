# Driving school management with a Django REST API

([Demo](https://gildas.le-drogoff.fr/car_crash/api/schema/swagger-ui/))

# Overview

This is a project made with the Django REST framework, it is an API that allows to manage a driving school, it
includes :

- Authentication with JWT tokens
- Display, pagination and sorting of beer references
- The management of orders, stocks
- Fine tuned permissions for the different users.
- Statistics display for an easy stock management

![Screenshot][image]

# Requirements

- Python 3.6+
- Django 4.1, 4.0, 3.2, 3.1, 3.0

# Installation

```bash
FIXTURES="./drivingschool/fixtures/*"

python -m venv venv
source ./venv/bin/activate
echo $(VIRTUAL_ENV) # Check if VIRTUAL_ENV is set

python -m pip install --upgrade pip setuptools wheel
pip install -r ./requirements.txt

cp .env.example .env

python manage.py migrate && \
for f in $FIXTURES
do
  echo "Processing $f file..."
  python manage.py loaddata "$f"
  ls "$f"
done
rm -rfv staticfiles;
python manage.py collectstatic
python manage.py runserver
```

```
GET http://127.0.0.1:8000/api/schema/swagger-ui/
```

<!-- # Example -->

<!-- [image]: ./references_list.png -->

<hr />

_Gildas Le Drogoff - 2023_


Mireille Roux


MDPMDPMDP

