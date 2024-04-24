from django.db import models
from django.db import models
from django.core.files.base import ContentFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
# Create your models here.
class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)
class WordFile(models.Model):
    file = models.FileField(upload_to='word_files/')
    upload_date = models.DateTimeField(auto_now_add=True)
class PDFFile(models.Model):
    pdf_file = models.FileField(upload_to='pdf_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class CompressedPDF(models.Model):
    original_pdf = models.FileField(upload_to='original_pdfs/')
    compressed_pdf = models.FileField(upload_to='compressed_pdfs/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
class imagefile(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
class UploadedPPT(models.Model):
    ppt_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# class Image1(models.Model):
#     image = models.ImageField(upload_to='imagespdf/')

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')

class UploadedFile(models.Model):
    pdf_file = models.FileField(upload_to='uploads/')
    word_file = models.FileField(upload_to='converted/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pdf_file.name

class Conversion(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    excel_file = models.FileField(upload_to='excels/')
    timestamp = models.DateTimeField(auto_now_add=True)


class PDFFile(models.Model):
    pdf_file = models.FileField(upload_to='pdf_files/')
    password = models.CharField(max_length=100)