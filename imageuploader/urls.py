from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from accounts import views
from accounts.views import register_view

app_name = 'pdf_compress'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('land/', include('farmers.urls', namespace='land')),
    path('', views.index),
    # path('word/', views.convert_word_to_pdf),
    # path('merge_pdfs/', views.merge_pdfs, name='merge_pdfs'),
    # path('compress_pdf/', views.compress_pdf, name='compress_pdf',),
    path('pdf2imageapp/', include('myapp.urls')),
    path('skn/', include('recommendation.urls')),

    # path('convert_ppt/', views.convert_ppt, name='convert_ppt'),
    # path('', views.imgtopdf, name="imgtopdf"),
    # path('jpgtopng', views.jpgtopng),
    # path('png', views.png),
    # path('upload-convert-download/', views.handle_file, name='upload-convert-download'),
    # path('pdfeoexel/', views.convert_pdf_to_excel, name='pdfeoexel'),
    # path('convert/', views.convert_pdf_to_excel, name='convert_pdf_to_excel'),
    # path('set_password/', views.set_password_to_pdf, name='set_password'),
    path('user/',views.user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
