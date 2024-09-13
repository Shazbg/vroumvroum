from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Garage(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=80)
    code_postal = models.IntegerField()
    def __str__(self):
        return self.nom

    
class Voiture(models.Model):
    immat = models.CharField(max_length=9)
    color = models.CharField(max_length=30)
    marque = models.CharField(max_length=30)
    modele = models.CharField(max_length=30)
    garage = models.ForeignKey(Garage,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="cars")

    def __str__(self):
        return self.immat

class Reservation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Réservation de {self.voiture.immat} par {self.user} du {self.date_debut} au {self.date_fin}"
    
    def clean(self):
        # Vérifier que la date de début est avant la date de fin
        if self.date_debut >= self.date_fin:
            raise ValidationError('La date de début doit être avant la date de fin.')

        # Vérifier la disponibilité de la voiture pour les dates choisies
        reservations = Reservation.objects.filter(voiture=self.voiture, statut='confirmee')
        for reservation in reservations:
            if (self.date_debut < reservation.date_fin) and (self.date_fin > reservation.date_debut):
                raise ValidationError('La voiture est déjà réservée pour cette période.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Cle(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return f"clé de {self.voiture}"



    

