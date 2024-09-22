#!/bin/bash
#Lancer les migrations à chaque lancement du container
python manage.py makemigrations 
python manage.py migrate  
