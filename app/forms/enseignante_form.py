from django.forms import ModelForm
from app.models import Enseignante

class EnseignanteForm(ModelForm):
    class Meta:
        model = Enseignante
        fields = '__all__'