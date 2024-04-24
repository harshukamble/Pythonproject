from django.contrib import admin
from .models import Image,WordFile,PDFFile, CompressedPDF, imagefile, UploadedPPT, UploadedImage, UploadedFile, Conversion
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']

@admin.register(WordFile)
class WordFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload_date')

@admin.register(CompressedPDF)
class CompressedPDFAdmin(admin.ModelAdmin):
    list_display = ('original_pdf', 'compressed_pdf', 'uploaded_at')

@admin.register(imagefile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('pdf',)

@admin.register(UploadedPPT)
class UploadedPPTAdmin(admin.ModelAdmin):
    list_display = ('ppt_file', 'uploaded_at')

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'word_file', 'uploaded_at')

@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'excel_file', 'timestamp')