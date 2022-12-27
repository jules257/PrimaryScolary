from django.forms import ModelForm
from app.models import Inscription

class InscriptionForm(ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'