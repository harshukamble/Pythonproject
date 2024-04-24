from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms
class signupForm(UserCreationForm): 
    number = forms.CharField(label='Number', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your number'}))
    categories_choices = [
        ('farmer', 'Farmer'),
        ('merchant', 'Merchant'),
        ('user', 'User'),
    ]
    categories = forms.ChoiceField(label='Categories', choices=categories_choices, widget=forms.Select(attrs={'class': 'input-field'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'number', 'categories']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email'}),
        }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TimeInput(attrs={'autofocus':True,'placeholder': 'username'}))
    password=forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'input-field','placeholder': 'pass'})) 

from django import forms
from .models import Image,WordFile,PDFFile,CompressedPDF,imagefile, UploadedPPT,UploadedImage,UploadedFile,Conversion, PDFFile
class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}
class Wordform(forms.ModelForm):
 class Meta:
  model = WordFile
  fields = '__all__'
  labels = {'file':''}
class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = '__all__'
        labels = {'file':''}
class CompressedPDFForm(forms.ModelForm):
    class Meta:
        model = CompressedPDF
        fields = ['original_pdf']
        widgets = {
            'original_pdf': forms.TextInput(attrs={'class': 'upload','type':'file'}),
        }
class imageFileForm(forms.ModelForm):
    class Meta:
        model = imagefile
        fields = ['pdf']
class UploadedPPTForm(forms.ModelForm):
    class Meta:
        model = UploadedPPT
        fields = ['ppt_file']
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['pdf_file']
class ConversionForm(forms.ModelForm):
    class Meta:
        model = Conversion
        fields = ['pdf_file']
class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['pdf_file', 'password']