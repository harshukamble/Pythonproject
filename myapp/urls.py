from django.urls import path
from . import views

urlpatterns = [
   path('pdf-to-images/', views.pdf_to_images, name='pdf_to_images'),
      path('word/', views.convert_word_to_pdf),
    path('merge_pdfs/', views.merge_pdfs, name='merge_pdfs'),
    path('compress_pdf/', views.compress_pdf, name='compress_pdf',),
    
    path('convert_ppt/', views.convert_ppt, name='convert_ppt'),
    path('imgtopdf/', views.imgtopdf, name="imgtopdf"),
    path('jpgtopng/', views.jpgtopng,name="jpgtopng"),
    path('png/', views.png,name='png'),
    path('upload-convert-download/', views.handle_file, name='upload-convert-download'),
    path('pdfeoexel/', views.convert_pdf_to_excel, name='pdfeoexel'),
    path('convert/', views.convert_pdf_to_excel, name='convert_pdf_to_excel'),
    path('set_password/', views.set_password_to_pdf, name='set_password'),
   #  path('user/',views.user),
]  