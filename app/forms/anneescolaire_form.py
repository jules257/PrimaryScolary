from django.forms import ModelForm
from app.models import Anneescolaire

class AnneescolaireForm(ModelForm):
    class Meta:
        model = Anneescolaire
        fields = '__all__'