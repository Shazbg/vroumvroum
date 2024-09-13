from django.shortcuts import render

from django.http import JsonResponse
from .models import Garage,Cle,Voiture, Reservation
from django.utils import timezone

now = timezone.now().date()

def garage_list(request):
    garages = Garage.objects.all()
    data = [{'id': garage.id, 'nom': garage.nom, 'adresse': garage.adresse, 'code_postal': garage.code_postal} for garage in garages]  # Créer une liste de dictionnaires
    return JsonResponse(data, safe=False)  # Renvoyer la liste au format JSON

def cle_list(request):
    cles = Cle.objects.all()
    data = [
        {
            'id': cle.id,
            'voiture': {
                'id': cle.voiture.id,
                'immat': cle.voiture.immat,
                'marque': cle.voiture.marque,
                'modele': cle.voiture.modele,
                'garage': cle.voiture.garage.nom
            } 
        }
        for cle in cles
    ]
    return JsonResponse(data, safe=False)

def voiture_list(request):
    voitures = Voiture.objects.all()
    data = [
        {
            'id': voiture.id,
            'immat': voiture.immat,
            'color': voiture.color,
            'marque': voiture.marque,
            'modele': voiture.modele,
            'photo_url': voiture.photo.url if voiture.photo else None,  # Gérer les cas sans photo
            'garage': {
                'id': voiture.garage.id,
                'nom': voiture.garage.nom,
                'adresse': voiture.garage.adresse,
                'code_postal': voiture.garage.code_postal
            },
            'reservations': [
                {
                    'id': reservation.id,
                    'date_debut': reservation.date_debut.strftime('%d/%m/%Y'),
                    'date_fin': reservation.date_fin.strftime('%d/%m/%Y'),
                }
                for reservation in Reservation.objects.filter(voiture=voiture, statut='confirmee', date_fin__gte=now)
            ]
        }
        for voiture in voitures
    ]
    return JsonResponse(data, safe=False)

def reservation_list(request):
    # Obtenir la date actuelle pour filtrer les réservations futures
    now = timezone.now().date()

    reservations = Reservation.objects.filter(date_fin__gte=now)
    data = [
        {
            'id': reservation.id,
            'date_debut': reservation.date_debut.strftime('%d/%m/%Y'),
            'date_fin': reservation.date_fin.strftime('%d/%m/%Y'),
            'voiture': {
                'id': reservation.voiture.id,
                'immat': reservation.voiture.immat,
                'marque': reservation.voiture.marque,
                'modele': reservation.voiture.modele,
                'color': reservation.voiture.color,
                'photo_url': reservation.voiture.photo.url if reservation.voiture.photo else None
            },
            'user': {
                'id': reservation.user.id,
                'username': reservation.user.username
            }
        }
        for reservation in reservations
    ]
    return JsonResponse(data, safe=False)
