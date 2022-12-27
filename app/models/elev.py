from django.db import models


SEXE = (('Garcon', 'garcon'), ('Fille', 'fille'))
class Elev(models.Model):
   
    
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    sexe = models.CharField(choices=SEXE, max_length=45)
    adresse = models.CharField( max_length=45)
    lieunaissance = models.CharField(max_length=45)

    def __str__(self):
        return self.nom+ " " +self.prenom



    
    
 
    
    
    