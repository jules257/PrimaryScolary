from django.db import models


class   Classe(models.Model):
    nom_classe = models.CharField(max_length=45)
  
    
    
    
    
    
    def __str__(self):
        return self.nom_classe