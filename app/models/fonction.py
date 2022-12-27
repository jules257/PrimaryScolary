from django.db import models
from app.models import Enseignante,Tache,Anneescolaire

class Fonction(models.Model):
  
    enseignante = models.ForeignKey(Enseignante,on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache,on_delete=models.CASCADE)
    anneescolaire = models.ForeignKey(Anneescolaire,on_delete=models.CASCADE)
    date = models.DateField(max_length=45)
  
    
    
    
    
    
  
   
    
    
 
    
    
    