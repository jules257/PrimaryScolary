from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Inscription
from app.forms import InscriptionForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# @login_required
def index(request):
     # permission
    # has_perm= False
    # if request.user.has_perm('app.delete_inscription','app.change_inscription'):
    #     has_perm = True
    
    assert isinstance(request,HttpRequest)
    
    inscriptions = Inscription.objects.all()
    return render(
        request,
        'app/inscriptions/index.html',
        {
            'inscriptions':inscriptions,
            # 'has_perm':has_perm
            
        }
    )
    
    
        
def create(request):
    form =InscriptionForm()
    return render(
        request,
        'app/inscriptions/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"inscription successfull saved")
        return redirect('/inscriptions')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = InscriptionForm()
        else:
            inscription = Inscription.objects.get(pk=id)
            form = InscriptionForm(instance=inscription)
        return render(
            request,
            'app/inscriptions/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = InscriptionForm(request.POST)
        else:
            inscription = Inscription.objects.get(pk=id)
            form = InscriptionForm(request.POST,instance=inscription)
        if form.is_valid():
            
            form.save()
            messages.success(request,"inscription successfull updated")
        return redirect('/inscriptions') 
    
def delete(request, id):
    inscription = Inscription.objects.get(pk=id)
    inscription.delete()
    return redirect('/inscriptions')         