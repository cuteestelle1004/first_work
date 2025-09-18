from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='cars_home2'),  # this serves /cars/
    path('drive/', views.drive, name='drive'),  # this serves /cars/drive/
]

