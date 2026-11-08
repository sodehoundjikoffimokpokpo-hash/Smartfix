from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('inscription/', views.inscrire_prestataire, name='inscription'),
]