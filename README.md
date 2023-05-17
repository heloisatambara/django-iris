# django-iris

# first commands:
## django-admin startproject irisCrud . | creates the initial template

## python manage.py runserver | runs the server

## python manage.py migrate | propagate changes made to the models

## python manage.py createsuperuser | creates the fisrst user, now you're able to login into url/admin
##  admin / admin


# adding iris to the project:
## pip install -r requirements.txt
## python manage.py migrate | remember to start iris - if it doensn't work restart it
## python manage.py startapp books | creates app
## python manage.py makemigrations | configure migrations - check __pycache__/0001_initial.py