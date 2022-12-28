from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Tache
from app.forms import TacheForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
    
    #  permission
    has_perm= False
    if request.user.has_perm('app.delete_tache','app.change_tache'):
        has_perm = True
    assert isinstance(request,HttpRequest)
    
    taches = Tache.objects.all()
    return render(
        request,
        'app/taches/index.html',
        {
            'taches':taches,
            'has_perm':has_perm
        
            
        }
    )
    
    
        
def create(request):
    form =TacheForm()
    return render(
        request,
        'app/taches/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"tache successfull saved")
        return redirect('/taches')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = TacheForm()
        else:
            tache = Tache.objects.get(pk=id)
            form = TacheForm(instance=tache)
        return render(
            request,
            'app/taches/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = TacheForm(request.POST)
        else:
            tache = Tache.objects.get(pk=id)
            form = TacheForm(request.POST,instance=tache)
        if form.is_valid():
            
            form.save()
            messages.success(request,"tache successfull updated")
        return redirect('/taches') 
    
def delete(request, id):
    tache = Tache.objects.get(pk=id)
    tache.delete()
    return redirect('/taches')         