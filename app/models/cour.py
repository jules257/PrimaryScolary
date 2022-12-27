from django.db import models

class Cour(models.Model):
  
    
    code_cours = models.CharField(max_length=45)
    nom_cours = models.CharField(max_length=45)
    
    
    
    
    def __str__(self):
        return self.code_cours+" "+self.nom_cours
   
    
    
 
    
    
    