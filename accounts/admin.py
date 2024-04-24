from django.contrib import admin
from .models import Image, WordFile, PDFFile, CompressedPDF, imagefile, UploadedPPT, UploadedImage, UploadedFile, Conversion

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'uploaded_at')  # Assuming 'uploaded_at' is a field in the PDFFile model

    def uploaded_at(self, obj):
        return obj.uploaded_at  # Replace 'uploaded_at' with the actual field name in your model

    uploaded_at.short_description = 'Uploaded At'  # Replace with a user-friendly display name
