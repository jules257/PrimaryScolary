from django.contrib import admin
from django.urls import path
from app.views import home,enseignantes,anneescolaires,elevs



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


    # path('cours/',cours.index, name='cours_index'),
    # path('cours/create', cours.create, name='cours_create'),
    # path('cours/store', cours.store, name='cours_store'),
    # path('cours/edit/<int:id>', cours.edit, name='cours_edit'),
    # path('cours/delete/<int:id>', cours.delete, name='cours_delete'),
    
    
    path('elevs/',elevs.index, name='elevs_index'),
    path('elevs/create', elevs.create, name='elevs_create'),
    path('elevs/store', elevs.store, name='elevs_store'),
    path('elevs/edit/<int:id>', elevs.edit, name='elevs_edit'),
    path('elevs/delete/<int:id>', elevs.delete, name='elevs_delete'),

    # path('parents/',parents.index, name='parents_index'),
    # path('parents/create', parents.create, name='parents_create'),
    # path('parents/store', parents.store, name='parents_store'),
    # path('parents/edit/<int:id>', parents.edit, name='parents_edit'),
    # path('parents/delete/<int:id>', parents.delete, name='parents_delete'),

    #  path('inscriptions/',inscriptions.index, name='inscriptions_index'),
    # path('inscriptions/create', inscriptions.create, name='inscriptions_create'),
    # path('inscriptions/store', inscriptions.store, name='inscriptions_store'),
    # path('inscriptions/edit/<int:id>', inscriptions.edit, name='inscriptions_edit'),
    # path('inscriptions/delete/<int:id>', inscriptions.delete, name='inscriptions_delete')
    
    
    
    
    
    
    
    
    
   
   
  
]