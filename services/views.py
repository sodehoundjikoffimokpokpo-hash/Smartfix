from django.shortcuts import render
from .models import Prestataire, Categorie

def home(request):
    prestataires = Prestataire.objects.filter(disponible=True)
    categories = Categorie.objects.all()
    
    context = {
        'prestataires': prestataires,
        'categories': categories,
    }
    return render(request, 'services/home.html', context)