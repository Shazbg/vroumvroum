<p align="center">
    <img src="https://github.com/user-attachments/assets/3ba5a526-c617-49c7-8165-30c3f3505d5c" width="300" alt="TSP logo">
</p>


# CSC 8567 - Projet Django et Docker

Auteur : Shazir Sheik

Ce projet est une plateforme de gestion de voitures, construite avec Django et déployée via Docker avec des conteneurs séparés pour deux applications distinctes : 
    - une application frontend (public) 
    - une API backend (api). 

Le projet utilise PostgreSQL comme base de données partagée entre les deux applications.

L'application **public** est la partie frontend du site web. Elle contient la page principale qui affiche la liste des voitures disponibles et la liste des garages. En cliquant sur une voiture, on obtient plus de détails sur celle-ci et sa disponibilité. Pour réserver une voiture, le bouton est disponible sur la page principale lorsqu'on est authentifié sur le site. Attention, il faut confirmer la réservation depuis le panel admin Django pour que celle-ci soit prise en compte !
Il est possible de créer un compte depuis la page principale, ou bien on peut se connecter avec le compte admin Django créé par défaut au lancement du container Docker **(admin/adminadmin)**

L'application **api** est une API au format JSON qui renvoit des informations telles que la liste des voitures, des garages ainsi que des clés.

## Liste des URLs accessibles :

    - http://localhost/public : page principale du site web
    - http://localhost/public/reservation : page de réservation d'un véhicule (accessible uniquement lorsque authentifié)
    - http://localhost/public/login : page de connexion
    - http://localhost/public/register : page de création de compte
    - http://localhost/public/logout : page de déconnexion, qui renvoit à la page principale
    - http://localhost/api/voitures : API qui renvoit la liste des voitures
    - http://localhost/api/garages : API qui renvoit la liste des garages
    - http://localhost/api/cles : API qui renvoit la liste des clés
    - http://localhost/admin : Panel admin Django intégré qui permet d'ajouter des voitures, garages, clés et confirmer les réservations


## Installation

**Il est recommandé d'utiliser un système d'exploitation type Linux.**
L'installation suivante fonctionne avec Docker et Docker-Compose

1. Dézippez l'archive du projet
```
tar -xvf **nomarchive**
```
   
2. Lancer la commande suivante
```
sudo docker compose up --build
```
Le site sera ainsi accessible aux adresses décrites juste au-dessus !

## Ajout de données

Le site fourni sera entièrement vierge et ne contiendra aucune voiture, garage, etc… Il est possible grâce à un petit script d'ajouter des données automatiquement afin de donner vie au site et de pouvoir tester toutes les fonctionnalités convenablement !

Pour cela, il faut lancer la commande suivante :
```
sudo docker exec -it vroumvroum-db-1 bash
```
Puis :
```
./load-dbdata.sh
```
Ce script va se charger de restorer la base de données postgresSQL avec des données sauvegardées dans un fichier **export.pgsql**.
Il est très fort possible que des erreurs s'affichent lors du lancement du script, cela est attendu et normal, cela est causé par le fait que la plupart des données existent déjà dans la table utilisée par Django.

Pour revenir à un site vierge si besoin, alors il suffit de supprimer le volume Docker bindé au container postgresSQL avec la commande suivante :
```
sudo docker volume rm **nomduvolume**
```
## Structure du projet
```
├── Dockerfile.api
├── Dockerfile.front
├── README.md
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── api.sh
├── database-schema.png
├── docker-compose.yaml
├── export.pgsql
├── load-dbdata.sh
├── manage.py
├── nginx.conf
├── public
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   │   └── public
│   ├── templates
│   │   └── public
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── voiture
    ├── asgi.py
    ├── media
    │   └── cars
    ├── settings
    │   ├── api.py
    │   ├── base.py
    │   └── public.py
    ├── urls-api.py
    ├── urls-public.py
    └── wsgi.py
```