from django.forms import ModelForm
from app.models import Classe

class ClasseForm(ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'