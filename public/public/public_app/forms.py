# forms.py
from django import forms
from api.models import Reservation  # Assurez-vous d'importer le modèle de réservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['voiture', 'date_debut', 'date_fin']
