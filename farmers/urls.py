from django.urls import path
from . import views

app_name = 'farmers'

urlpatterns = [
    path('register/farmer/', views.farmer_registration, name='farmer_registration'),
    path('register/landowner/', views.landowner_registration, name='landowner_registration'),
    path('success/', views.registration_success, name='success'),
    path('matching_landowners/<int:farmer_id>/', views.matching_landowners, name='matching_landowners'),  # New URL pattern
]
