from django.contrib import admin
from django.urls import path
from app.views import home,enseignantes,anneescolaires



urlpatterns = [
    path('',home.index, name='home'),
    
    path('enseignantes/',enseignantes.index, name='enseignantes_index'),
    path('enseignantes/create',enseignantes.create, name='enseignantes_create'),
    path('enseignantes/store', enseignantes.store, name='enseignantes_store'),
    path('enseignantes/edit/<int:id>', enseignantes.edit, name='enseignantes_edit'),
    path('enseignantes/delete/<int:id>',enseignantes.delete, name='enseignantes_delete'),
    
     
    path('anneescolaires/',anneescolaires.index, name='anneescolaires_index'),
    path('anneescolaires/create', anneescolaires.create, name='anneescolaires_create'),
    path('anneescolaires/store', anneescolaires.store, name='anneescolaires_store'),
    path('anneescolaires/edit/<int:id>', anneescolaires.edit, name='anneescolaires_edit'),
    path('anneescolaires/delete/<int:id>', anneescolaires.delete, name='anneescolaires_delete'),
    
    
    
    
    
   
   
  
]