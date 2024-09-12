from django.db import models
from django.core.exceptions import ValidationError


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

class Cle(models.Model):
    etat_pret = models.BooleanField()
    date_pret = models.DateField(blank=True, null=True)
    date_rendu = models.DateField(blank=True, null=True)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def clean(self):
        if self.etat_pret:
            if not self.date_pret or not self.date_rendu:
                raise ValidationError("Les champs 'date_pret' et 'date_rendu' sont obligatoires si 'etat_pret' est vrai.")
            if self.date_pret > self.date_rendu:
                raise ValidationError("'date_pret' doit être antérieure ou égale à 'date_rendu'.")
        else:
            if self.date_pret or self.date_rendu:
                raise ValidationError("Les champs 'date_pret' et 'date_rendu' doivent être vides si 'etat_pret' est faux.")

    def save(self, *args, **kwargs):
        # merci chatGPT
        self.clean()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"clé de {self.voiture}"



    

