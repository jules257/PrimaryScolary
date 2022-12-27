from django.db import models

SEXE = (('Homme', 'homme'), ('Femme', 'femme'))

class Enseignante(models.Model):
    matricule = models.CharField(max_length=45)
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adresse = models.CharField(max_length=45)
    sexe = models.CharField(choices=SEXE, max_length=45)
    tel = models.CharField(max_length=45)
    datenaissance = models.DateField(max_length=45)
    


    
    
    
    
    
    def __str__(self):
        return self.nom+" "+self.prenom +" "+self.matricule



    
    
    
    