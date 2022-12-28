from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Parent
from app.forms import ParentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
    
     # permission
    has_perm= False
    if request.user.has_perm('app.delete_parent','app.change_parent'):
        has_perm = True
    assert isinstance(request,HttpRequest)
    
    parents = Parent.objects.all()
    return render(
        request,
        'app/parents/index.html',
        {
            'parents':parents,
            'has_perm':has_perm
           
            
        }
    )
    
    
        
def create(request):
    form =ParentForm()
    return render(
        request,
        'app/parents/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"parent successfull saved")
        return redirect('/parents')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = ParentForm()
        else:
            parent = Parent.objects.get(pk=id)
            form = ParentForm(instance=parent)
        return render(
            request,
            'app/parents/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = ParentForm(request.POST)
        else:
            parent = Parent.objects.get(pk=id)
            form = ParentForm(request.POST,instance=parent)
        if form.is_valid():
            
            form.save()
            messages.success(request,"parent successfull updated")
        return redirect('/parents') 
    
def delete(request, id):
    parent = Parent.objects.get(pk=id)
    parent.delete()
    return redirect('/parents')         