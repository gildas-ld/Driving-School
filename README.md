# Bar management with a Django REST API

([Demo](https://gildas.le-drogoff.fr/my_bar/api/schema/swagger-ui/))

# Overview

This is a project made with the Django REST framework, it is an API that allows to manage a bar, it includes :

- Authentication with JWT tokens
- Display, pagination and sorting of beer references
- The management of orders, stocks
- Fine tuned permissions for the different users (CEO, bartenders, customers).
- Statistics display for an easy stock management

![Screenshot][image]

# Requirements

- Python 3.6+
- Django 4.1, 4.0, 3.2, 3.1, 3.0

# Installation

```bash
python -m venv venv
source ./venv/bin/activate
echo $(VIRTUAL_ENV) # Check if VIRTUAL_ENV is set

python -m pip install --upgrade pip setuptools wheel
pip install -r ./requirements.txt

cp .env.example .env

python manage.py migrate
python manage.py loaddata ./drivingschool/fixtures/0000_all.json
python manage.py collectstatic
python manage.py runserver
```

```
GET http://127.0.0.1:8000/api/schema/swagger-ui/
GET http://127.0.0.1:8000/api/references/
```

# Example

### References

```
GET http://127.0.0.1:8000/api/references/
```

```json
{
  "count": 50,
  "next": "http://127.0.0.1:8000/api/references/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "ref": "007",
      "name": "007",
      "description": "Light and hoppy.",
      "availability": 331,
      "where": ["rooftop", "3ème étage"]
    },
    {
      "id": 2,
      "ref": "100",
      "name": "100",
      "description": "A super smooth ruby ale. Traditional in its design...",
      "availability": 695,
      "where": ["rooftop", "1er étage", "3ème étage"]
    },
    {"..."}
  ]
}
```

### Bars

```
GET http://127.0.0.1:8000/api/bars/
```

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "1er étage"
    },
    {
      "id": 2,
      "name": "2ème étage"
    },
    {"..."},
    {
      "id": 5,
      "name": "skyscrapper"
    }
  ]
}
```

### Stocks

```
GET http://127.0.0.1:8000/api/stocks?bar=2
```

```json
{
  "count": 10,
  "results": [
    {
      "reference": 34,
      "bar": 2,
      "stock": 198
    },
    {
      "reference": 6,
      "bar": 2,
      "stock": 194
    },
    {"..."}
  ]
}
```

### Statistics

```
GET http://127.0.0.1:8000/api/statistics/
```

```json
{
  "all_stock": {
    "description": "Liste des comptoirs qui ont toutes les références en stock",
    "nombre": 1,
    "bar": [
      {
        "bar": 4,
        "total": 50
      }
    ]
  },
  "miss_at_least_one": {
    "description": "Liste des comptoirs qui ont au moins une référence épuisée",
    "nombre": 2,
    "bar": [
      {
        "bar": 1,
        "total": 6
      },
      {
        "bar": 2,
        "total": 10
      }
    ]
  },
  "list_of_missing_references": {
    "description": "Liste des références manquantes par bar",
    "references": [
      {
        "bar": 1,
        "missing_references": ["3point8_Lager", "65_Mild_Brown_Ale", "3_/_6"]
      },
      {
        "bar": 2,
        "missing_references": [
          "3B's",
          "1066",
          "1911_Celebration_Ale",
          "1st_Lite"
        ]
      },
      {
        "bar": 3,
        "missing_references": [
          "92_Squadron",
          "1767_Founders_Ale",
          "1880_Ale",
          "22",
          "2B's",
          "3point8_Lager",
          "11_Knights_in_Brazil",
          "1832_Cuckold_Alley_Ale"
        ]
      }
    ]
  }
}
```

[image]: ./references_list.png

<hr />

_Gildas Le Drogoff - 2022_
