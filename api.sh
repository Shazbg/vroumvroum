#!/bin/bash
#Lancer les migrations à chaque lancement du container
python manage.py makemigrations --settings=voiture.settings.api
python manage.py migrate --settings=voiture.settings.api

#Création auto d'un login admin/adminadmin pour accéder au panel Django admin (localhost/admin)
python manage.py createsuperuser --noinput --username=admin --settings=voiture.settings.api
python manage.py runserver 0.0.0.0:8001 --settings=voiture.settings.api