from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Attribution
from app.forms import AttributionForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # permission
    has_perm= False
    if request.user.has_perm('app.delete_attribution','app.change_attribution'):
       has_perm = True
    assert isinstance(request,HttpRequest)
    
    attributions = Attribution.objects.all()
    return render(
        request,
        'app/attributions/index.html',
        {
            'attributions':attributions,
            'has_perm':has_perm
            
            
        }
    )
    
    
        
def create(request):
    form =AttributionForm()
    return render(
        request,
        'app/attributions/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = AttributionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"attribution successfull saved")
           
        return redirect('/attributions')
    
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = AttributionForm()
        else:
            attribution = Attribution.objects.get(pk=id)
            form = AttributionForm(instance=attribution)
        return render(
            request,
            'app/attributions/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = AttributionForm(request.POST)
        else:
            attribution = Attribution.objects.get(pk=id)
            form = AttributionForm(request.POST,instance=attribution)
        if form.is_valid():
            
            form.save()
            messages.success(request,"attribution successfull updated")
        return redirect('/attributions') 
    
def delete(request, id):
    attribution = Attribution.objects.get(pk=id)
    attribution.delete()
    return redirect('/attributions')         