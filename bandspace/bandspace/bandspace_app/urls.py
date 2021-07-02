from django.urls import path
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),
]