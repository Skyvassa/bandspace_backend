from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('bands/', views.get_bands, name='get_bands'),
    path('bands/<int:pk>/', views.get_user, name='get_user')
]