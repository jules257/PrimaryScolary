from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Cour
from app.forms import CourForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
      # permission
    has_perm= False
    if request.user.has_perm('app.delete_cour','app.change_cour'):
        has_perm = True
    assert isinstance(request,HttpRequest)
    
    cours = Cour.objects.all()
    return render(
        request,
        'app/cours/index.html',
        {
            'cours':cours,
            'has_perm':has_perm
            
        }
    )
    
    
        
def create(request):
    form =CourForm()
    return render(
        request,
        'app/cours/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = CourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"cours successfull saved")
        return redirect('/cours')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = CourForm()
        else:
            cour = Cour.objects.get(pk=id)
            form = CourForm(instance=cour)
        return render(
            request,
            'app/cours/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = CourForm(request.POST)
        else:
            cour = Cour.objects.get(pk=id)
            form = CourForm(request.POST,instance=cour)
        if form.is_valid():
            
            form.save()
            messages.success(request,"cours successfull updated")
        return redirect('/cours') 
    
def delete(request, id):
    cour = Cour.objects.get(pk=id)
    cour.delete()
    return redirect('/cours')         