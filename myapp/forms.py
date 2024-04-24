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