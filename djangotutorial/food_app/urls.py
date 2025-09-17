from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('go/', price, name='price'),
    path('sleep/', sleep, name='sleep'),
]


