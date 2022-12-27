from django.forms import ModelForm
from app.models import Cour

class CourForm(ModelForm):
    class Meta:
        model = Cour
        fields = '__all__'