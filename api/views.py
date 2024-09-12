from django.shortcuts import render

from django.http import JsonResponse
from .models import Garage,Cle,Voiture

def garage_list(request):
    garages = Garage.objects.all()
    data = [{'id': garage.id, 'nom': garage.nom, 'adresse': garage.adresse, 'code_postal': garage.code_postal} for garage in garages]  # Créer une liste de dictionnaires
    return JsonResponse(data, safe=False)  # Renvoyer la liste au format JSON

def cle_list(request):
    cles = Cle.objects.all()
    data = [
        {
            'id': cle.id,
            'etat_pret': cle.etat_pret,
            'date_pret': cle.date_pret,
            'date_rendu': cle.date_rendu,
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
            'photo_url': voiture.photo.url,
            'garage': {'id': voiture.garage.id, 'nom': voiture.garage.nom, 'adresse': voiture.garage.adresse, 'code_postal': voiture.garage.code_postal}
        }
        for voiture in voitures
    ]
    return JsonResponse(data, safe=False)
