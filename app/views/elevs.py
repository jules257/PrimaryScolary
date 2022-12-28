from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Elev
from app.forms import ElevForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
      # permission
    has_perm= False
    if request.user.has_perm('app.delete_elev','app.change_elev'):
        has_perm = True
    assert isinstance(request,HttpRequest)
    
    elevs = Elev.objects.all()
    return render(
        request,
        'app/elevs/index.html',
        {
            'elevs':elevs,
            'has_perm':has_perm
            
        }
    )
    
    
        
def create(request):
    form =ElevForm()
    return render(
        request,
        'app/elevs/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = ElevForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"eleve successfull saved")
        return redirect('/elevs')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = ElevForm()
        else:
            elev = Elev.objects.get(pk=id)
            form = ElevForm(instance=elev)
        return render(
            request,
            'app/elevs/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = ElevForm(request.POST)
        else:
            elev = Elev.objects.get(pk=id)
            form = ElevForm(request.POST,instance=elev)
        if form.is_valid():
            
            form.save()
            messages.success(request,"eleve successfull updated")
        return redirect('/elevs') 
    
def delete(request, id):
    elev = Elev.objects.get(pk=id)
    elev.delete()
    return redirect('/elevs')         