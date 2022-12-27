from django.db import models
from app.models import Elev,Parent,Anneescolaire,Classe

class Inscription(models.Model):
    elev = models.ForeignKey(Elev,on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE)
    anneescolaire = models.ForeignKey(Anneescolaire,on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe(),on_delete=models.CASCADE)
    date = models.DateField(max_length=45)
    
    
    
    
    
    
    
    
    
  
   
    
    
 
    
    
    