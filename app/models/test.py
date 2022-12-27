from django.db import models
from app.models import Cour,Classe,Enseignante,Anneescolaire

PERIODE = (('Trimestre 1', 'trimestre 1'), ('Trimestre 2', 'trimestre 2'),('Trimestre 3','trimestre 3'))
class Test(models.Model):
    cour = models.ForeignKey(Cour,on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    enseignante = models.ForeignKey(Enseignante,on_delete=models.CASCADE)
    anneescolaire = models.ForeignKey(Anneescolaire,on_delete=models.CASCADE)
    date = models.DateField(max_length=45)
    type = models.CharField(max_length=45)
    periode = models.CharField(choices=PERIODE, max_length=45)

    
    
    
    
    
  
   
    
    
 
    
    
    