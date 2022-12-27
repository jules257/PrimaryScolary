from django.db import models


class  Tache(models.Model):
    nom_tache = models.CharField(max_length=45)
  
    
    
    
    
    
    def __str__(self):
        return self.nom_tache