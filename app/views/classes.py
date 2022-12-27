from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Classe
from app.forms import ClasseForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
      # permission
    # has_perm= False
    # if request.user.has_perm('app.delete_classe','app.change_classe'):
    #     has_perm = True
    assert isinstance(request,HttpRequest)
    
    classes = Classe.objects.all()
    return render(
        request,
        'app/classes/index.html',
        {
            'classes':classes,
            # 'has_perm':has_perm
            
        }
    )
    
    
        
def create(request):
    form =ClasseForm()
    return render(
        request,
        'app/classes/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"classe successfull saved")
           
        return redirect('/classes')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = ClasseForm()
        else:
            classe = Classe.objects.get(pk=id)
            form = ClasseForm(instance=classe)
        return render(
            request,
            'app/classes/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = ClasseForm(request.POST)
        else:
            classe = Classe.objects.get(pk=id)
            form = ClasseForm(request.POST,instance=classe)
        if form.is_valid():
            
            form.save()
            messages.success(request,"classe successfull updated")
        return redirect('/classes') 
    
def delete(request, id):
    classe = Classe.objects.get(pk=id)
    classe.delete()
    return redirect('/classes')         