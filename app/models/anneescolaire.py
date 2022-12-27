from django.db import models


class Anneescolaire(models.Model):
    anneescolaire = models.CharField(max_length=45)
  
    
    
    
    
    
    def __str__(self):
        return self.anneescolaire