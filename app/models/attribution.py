from django.db import models
from app.models import Enseignante,Classe,Cour,Anneescolaire

class Attribution(models.Model):
    enseignante = models.ForeignKey(Enseignante,on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    cour = models.ForeignKey(Cour,on_delete=models.CASCADE)
    anneescolaire = models.ForeignKey(Anneescolaire,on_delete=models.CASCADE)
    date = models.DateField(max_length=45)
  
    
    
    
    
    
  
   
    
    
 
    
    
    