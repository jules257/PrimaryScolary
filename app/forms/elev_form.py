from django.forms import ModelForm
from app.models import Elev

class ElevForm(ModelForm):
    class Meta:
        model = Elev
        fields = '__all__'