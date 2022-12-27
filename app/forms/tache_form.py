from django.forms import ModelForm
from app.models import Tache

class TacheForm(ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'