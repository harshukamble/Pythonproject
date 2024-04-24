from django import forms
from .models import Farmer, LandOwner

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['mobile_number', 'land_quantity_sq_ft', 'city']

class LandOwnerForm(forms.ModelForm):
    # Define the extra fields
    full_name = forms.CharField(max_length=100)
    document = forms.FileField()

    class Meta:
        model = LandOwner
        fields = ['full_name', 'mobile_number', 'land_quantity_sq_ft', 'city', 'document']
