from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Fonction
from app.forms import FonctionForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
    
     # permission
   
    assert isinstance(request,HttpRequest)
    
    fonctions = Fonction.objects.all()
    return render(
        request,
        'app/Fonctions/index.html',
        {
            'fonctions':fonctions,
            
            
        }
    )
    
    
        
def create(request):
    form =FonctionForm()
    return render(
        request,
        'app/fonctions/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = FonctionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"fonction successfull saved")
           
        return redirect('/fonctions')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = FonctionForm()
        else:
            fonction = Fonction.objects.get(pk=id)
            form = FonctionForm(instance=fonction)
        return render(
            request,
            'app/fonctions/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = FonctionForm(request.POST)
        else:
            fonction = Fonction.objects.get(pk=id)
            form = FonctionForm(request.POST,instance=fonction)
        if form.is_valid():
            
            form.save()
            messages.success(request,"fonction successfull updated")
        return redirect('/fonctions') 
    
def delete(request, id):
    fonction = Fonction.objects.get(pk=id)
    fonction.delete()
    return redirect('/fonctions')         