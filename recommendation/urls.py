from django.contrib import admin
from django.urls import path
from recommendation import views
urlpatterns = [
    path('fertilizer_predict/', views.fert_recommend, name='fertilizer_predict'),
    path('crop-predict/', views.indexrec, name='crop-predict'),
]   