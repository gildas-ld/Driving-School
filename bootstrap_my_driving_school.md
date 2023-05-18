## My driving school (bootstrap)

### W1 - Python (W-WEB-W4)

```
delivery method : BSdrivingschool on Github
build tool : no need here
```

- The totality of your source files, except all useless files (binary, temp files, obj
    files,...), must be included in your delivery.
- All the bonus files (including a potential specific Makefile) should be in a directory
    named _bonus_.
- Error messages have to be written on the error output, and the program should
    then exit with the 84 error code (0 if there is no error).


## Introduction

Votre mission, si vous l’acceptez (mais en même temps, avez-vous vraiment le choix? :p), est de réaliser
une authentification avec django et avec une base de donnee SQLite.

## Notions abordées

- Framework Django
- Base de données SQLite
- Routes
- Création d’une authentification


## Projet

Dans ce bootstrap vous allez apprendre a vous servir d’une base de donnee SQLite afin de recoder une
authentification.
Vous allez pour cela dans un premier temps installer le necessaire pour realiser ce bootstrap.
https://www.djangoproject.com/download/ pour le framework django
[http://www.sqlitetutorial.net/sqlite-python/](http://www.sqlitetutorial.net/sqlite-python/) pour la Base de donnee.

```
Tout ce dont vous avez besoin ce trouve sur la documentation de django!
```
Le premier point important est de setup tout l’environement

- créer un dossier bootstrap qui va etre le dossier dans lequel on va coder
- installer Django avec Pipenv
- lancer l’environnement virtuel avec pipenv
- créer un nouveau projet django appelle my_project
- créer une database sqlite avec migrate
- lancer le serveur local

Ensuite, il faudra créer notre page login (HTML, template) ainsi que créer notre routeur et les routes corre-
spondantes: Route1, Route2. Vous trouverez toutes les information necessaire sur la documentation django.
Il vous faudra créer des users avec manage superuser afin d’avoir le systeme d’aministration.


Voici les commandes a lancer dans le dépot pour initialiser votre projet :

### ∇ Terminal - + x

```
∼/W-WEB-350> pipenv install django==2.
∼/W-WEB-350> pipenv shell
∼/W-WEB-350> (bootstrap_python_my_driving_school) django-admin.py startproject
my_project.
∼/W-WEB-350> (bootstrap_python_my_driving_school) python manage.py migrate
∼/W-WEB-350> (bootstrap_python_my_driving_school) python manage.py runserver
```
## Liens Utiles!

Regarder ces tutoriel, ils vous permettent de realiser une base de projet! :

- Login / logout avec django
- Inscription en bdd
- Vidéo intéressante



