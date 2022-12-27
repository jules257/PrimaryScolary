from django.db import models


class Parent(models.Model):
   
    
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    adresse = models.CharField( max_length=45)
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.nom+ " " +self.prenom+" "+self.tel

    
    
 
    
    
    