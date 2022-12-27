from django.forms import ModelForm
from app.models import Parent

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'