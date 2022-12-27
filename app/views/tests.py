from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Test
from app.forms import TestForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def index(request):
      # permission
    # has_perm= False
    # if request.user.has_perm('app.delete_test','app.change_test'):
    #     has_perm = True
    assert isinstance(request,HttpRequest)
    
    tests = Test.objects.all()
    return render(
        request,
        'app/tests/index.html',
        {
            'tests':tests,
            
            
        }
    )
    
    
        
def create(request):
    form =TestForm()
    return render(
        request,
        'app/tests/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"test successfull saved")
        return redirect('/tests')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = TestForm()
        else:
            test = Test.objects.get(pk=id)
            form = TestForm(instance=test)
        return render(
            request,
            'app/tests/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = TestForm(request.POST)
        else:
            test = Test.objects.get(pk=id)
            form = TestForm(request.POST,instance=test)
        if form.is_valid():
            
            form.save()
            messages.success(request,"test successfull updated")
        return redirect('/tests') 
    
def delete(request, id):
    test = Test.objects.get(pk=id)
    test.delete()
    return redirect('/tests')         