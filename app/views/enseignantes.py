from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Enseignante
from app.forms import EnseignanteForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
      # permission
    has_perm= False
    if request.user.has_perm('app.delete_enseignante','app.change_enseignante'):
        has_perm = True
    assert isinstance(request,HttpRequest)
    
    enseignantes = Enseignante.objects.all()
    return render(
        request,
        'app/enseignantes/index.html',
        {
            'enseignantes':enseignantes,
            'has_perm':has_perm
            
            
        }
    )
    
    
        
def create(request):
    form =EnseignanteForm()
    return render(
        request,
        'app/enseignantes/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = EnseignanteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"enseignant successfull saved")
        return redirect('/enseignantes')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = EnseignanteForm()
        else:
            enseignante = Enseignante.objects.get(pk=id)
            form = EnseignanteForm(instance=elev)
        return render(
            request,
            'app/enseignantes/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = EnseignanteForm(request.POST)
        else:
            enseignante = Enseignante.objects.get(pk=id)
            form = EnseignanteForm(request.POST,instance=enseignante)
        if form.is_valid():
            
            form.save()
            messages.success(request,"enseignant successfull updated")
        return redirect('/enseignantes') 
    
def delete(request, id):
    enseignante = Enseignante.objects.get(pk=id)
    enseignante.delete()
    return redirect('/enseignantes')         