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
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return f"clé de {self.voiture}"



    

