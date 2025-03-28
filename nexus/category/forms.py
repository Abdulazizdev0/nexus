from django import forms
from .models import Region,Brand

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'