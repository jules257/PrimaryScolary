from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Anneescolaire
from app.forms import AnneescolaireForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # permission
    has_perm= False
    if request.user.has_perm('app.delete_anneescolaire','app.change_anneescolaire'):
        has_perm = True
   
    assert isinstance(request,HttpRequest)
    
    anneescolaires = Anneescolaire.objects.all()
    return render(
        request,
        'app/anneescolaires/index.html',
        {
            'anneescolaires':anneescolaires,
            'has_perm':has_perm
            
            
        }
    )
    
    
        
def create(request):
    form =AnneescolaireForm()
    return render(
        request,
        'app/anneescolaires/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = AnneescolaireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"year successfull saved")
           
        return redirect('/anneescolaires')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = AnneescolaireForm()
        else:
            anneescolaire = Anneescolaire.objects.get(pk=id)
            form = AnneescolaireForm(instance=anneescolaire)
        return render(
            request,
            'app/anneescolaires/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = AnneescolaireForm(request.POST)
        else:
            anneescolaire = Anneescolaire.objects.get(pk=id)
            form = AnneescolaireForm(request.POST,instance=anneescolaire)
        if form.is_valid():
            
            form.save()
            messages.success(request,"year successfull updated")
        return redirect('/anneescolaires') 
    
def delete(request, id):
    anneescolaire = Anneescolaire.objects.get(pk=id)
    anneescolaire.delete()
    return redirect('/anneescolaires')         