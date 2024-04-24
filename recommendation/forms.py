from django import forms
from .models import SoilContent

class SoilContentForm(forms.ModelForm):
    class Meta:
        model = SoilContent
        fields = ['nitrogen', 'phosphorus', 'potassium', 'ph_level']
        widgets = {
            'nitrogen': forms.NumberInput(attrs={'class': 'form-control'}),
            'phosphorus': forms.NumberInput(attrs={'class': 'form-control'}),
            'potassium': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LocationForm(forms.Form):
    location = forms.CharField(label='Enter your location:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields.update(SoilContentForm().fields)
