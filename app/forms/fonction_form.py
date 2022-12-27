from django.forms import ModelForm
from app.models import Fonction

class FonctionForm(ModelForm):
    class Meta:
        model = Fonction
        fields = '__all__'