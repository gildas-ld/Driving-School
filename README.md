# Driving School

<!-- ([Demo](https://gildas.le-drogoff.fr/car_crash/api/schema/swagger-ui/)) -->

## Overview

Welcome to the Driving School ! This is a project made with the Django REST framework. It is designed to streamline the interactions between students, instructors, secretaries, and administrators.

## Tech Stack

**Client & Server :** Django

## Features

### 🎓 Student Account

- **Student Profile** : Access to personal information, ensuring that all details are up-to-date and accurate.
- **Schedule Overview** : A clear view of the student's daily and weekly schedule.
- **Hourly Tracker** : A built-in system to display the total hours allocated to the student and how many have been used.

### 📚 Instructor Account

- **Personal Schedule** : Instructors can view their timetable to keep track of their appointments.
- **Student Records** : An easy-to-access panel for viewing detailed student information.
- **Appointment Manager** : Allows instructors to add, modify, or delete appointments with students.

### 🗂 Secretary Account

- **Account Management** :
  - Add, modify, or delete Student and Instructor accounts, ensuring the up-to-date listing of all individuals.
- **Student File Access** : View detailed student files for academic and administrative purposes.
- **Time Allocator** : Grant additional hours to students when necessary.
- **Appointment Oversight** : An enhanced version of the Instructor's appointment manager, enabling the addition, modification, or deletion of any Student or Instructor appointments.
- **Schedule Viewers** :
  - View individual Student or Instructor schedules.
  - Access to the institution's general schedule to oversee all activities.

### 👑 Admin Account

- **All Secretary Privileges** : Admins have full access to all the functionalities offered to the Secretary account.
- **Secretary Account Management** : The power to add, modify, or delete Secretary accounts, ensuring the right individuals have access to sensitive functionalities.

### Requirements

- Python 3.6+
- Django 4.2, 4.1, 4.0, 3.2, 3.1, 3.0

### Installation

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

### Users in fixtures

| username          | email                        | user_type  |
| :---------------- | :--------------------------- | :--------- |
| Briony Taylor     | b.taylor@epitech.eu          | Admin      |
| Gérald Le Coq     | gerald.le-coq@epitech.eu     | Admin      |
| Alberte Bonnet    | alberte.bonnet@epitech.eu    | Instructor |
| Alen Cunningham   | a.cunningham@epitech.eu      | Instructor |
| Alfred Douglas    | a.douglas@epitech.eu         | Instructor |
| Emily Sullivan    | e.sullivan@epitech.eu        | Instructor |
| James Clark       | j.clark@epitech.eu           | Instructor |
| Jordan Scott      | j.scott@epitech.eu           | Instructor |
| Julian Craig      | j.craig@epitech.eu           | Instructor |
| Kelsey Carroll    | k.carroll@epitech.eu         | Instructor |
| Mireille Roux     | mireille.roux@epitech.eu     | Instructor |
| Robert Dupond     | robert.dupond@epitech.eu     | Instructor |
| Carl Miller       | c.miller@epitech.eu          | Secretary  |
| Melissa Bailey    | m.bailey@epitech.eu          | Secretary  |
| Olga Ortega       | olga.ortega@epitech.eu       | Secretary  |
| Steven Carroll    | s.carroll@epitech.eu         | Secretary  |
| Albert Holmes     | a.holmes@epitech.eu          | Student    |
| Alina Morgan      | a.morgan@epitech.eu          | Student    |
| Fiona Stevens     | f.stevens@epitech.eu         | Student    |
| Gildas Le Drogoff | gildas.le-drogoff@epitech.eu | Student    |
| Hugo Dutreuil     | hugo.dutreuil@epitech.eu     | Student    |
| Jack Campbell     | j.campbell@epitech.eu        | Student    |
| James Hawkins     | j.hawkins@epitech.eu         | Student    |
| Lucy Anderson     | l.anderson@epitech.eu        | Student    |
| Ned Ellis         | n.ellis@epitech.eu           | Student    |
| Oliver Fowler     | o.fowler@epitech.eu          | Student    |
| Paul Evans        | p.evans@epitech.eu           | Student    |

<hr />

_Gildas Le Drogoff - 2023_

<!-- Mireille Roux

MDPMDPMDP -->
