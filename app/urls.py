from django.contrib import admin
from django.urls import path
from app.views import home,enseignantes,anneescolaires,elevs,parents,classes,cours,tests,taches,inscriptions,attributions,fonctions



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


    path('cours/',cours.index, name='cours_index'),
    path('cours/create', cours.create, name='cours_create'),
    path('cours/store', cours.store, name='cours_store'),
    path('cours/edit/<int:id>', cours.edit, name='cours_edit'),
    path('cours/delete/<int:id>', cours.delete, name='cours_delete'),
    
    
    path('elevs/',elevs.index, name='elevs_index'),
    path('elevs/create', elevs.create, name='elevs_create'),
    path('elevs/store', elevs.store, name='elevs_store'),
    path('elevs/edit/<int:id>', elevs.edit, name='elevs_edit'),
    path('elevs/delete/<int:id>', elevs.delete, name='elevs_delete'),

    path('parents/',parents.index, name='parents_index'),
    path('parents/create', parents.create, name='parents_create'),
    path('parents/store', parents.store, name='parents_store'),
    path('parents/edit/<int:id>', parents.edit, name='parents_edit'),
    path('parents/delete/<int:id>', parents.delete, name='parents_delete'),


    path('classes/',classes.index, name='classes_index'),
    path('classes/create', classes.create, name='classes_create'),
    path('classes/store', classes.store, name='classes_store'),
    path('classes/edit/<int:id>', classes.edit, name='classes_edit'),
    path('classes/delete/<int:id>', classes.delete, name='classes_delete'),


    
    path('tests/',tests.index, name='tests_index'),
    path('tests/create', tests.create, name='tests_create'),
    path('tests/store', tests.store, name='tests_store'),
    path('tests/edit/<int:id>', tests.edit, name='tests_edit'),
    path('tests/delete/<int:id>', tests.delete, name='tests_delete'),
    
    
    path('taches/',taches.index, name='taches_index'),
    path('taches/create',taches.create, name='taches_create'),
    path('taches/store', taches.store, name='taches_store'),
    path('taches/edit/<int:id>', taches.edit, name='taches_edit'),
    path('taches/delete/<int:id>',taches.delete, name='taches_delete'),
    
    
    path('inscriptions/',inscriptions.index, name='inscriptions_index'),
    path('inscriptions/create', inscriptions.create, name='inscriptions_create'),
    path('inscriptions/store', inscriptions.store, name='inscriptions_store'),
    path('inscriptions/edit/<int:id>', inscriptions.edit, name='inscriptions_edit'),
    path('inscriptions/delete/<int:id>', inscriptions.delete, name='inscriptions_delete'),
    
    
    path('attributions/',attributions.index, name='attributions_index'),
    path('attributions/create', attributions.create, name='attributions_create'),
    path('attributions/store', attributions.store, name='attributions_store'),
    path('attributions/edit/<int:id>', attributions.edit, name='attributions_edit'),
    path('attributions/delete/<int:id>', attributions.delete, name='attributions_delete'),
    
    path('fonctions/',fonctions.index, name='fonctions_index'),
    path('fonctions/create', fonctions.create, name='fonctions_create'),
    path('fonctions/store', fonctions.store, name='fonctions_store'),
    path('fonctions/edit/<int:id>', fonctions.edit, name='fonctions_edit'),
    path('fonctions/delete/<int:id>', fonctions.delete, name='fonctions_delete'),
    
    
    
    
    
    
    
    
    
   
   
  
]