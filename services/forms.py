from django import forms
from .models import Prestataire

class PrestataireRegistrationForm(forms.ModelForm):
    class Meta:
        model = Prestataire
        fields = ['nom_complet', 'categorie', 'telephone', 'quartier', 'tarif_journalier']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm', 'placeholder': 'Ex: Koffi Sodehoundji'}),
            'categorie': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm bg-white'}),
            'telephone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm', 'placeholder': 'Ex: +228 90 00 00 00'}),
            'quartier': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm', 'placeholder': 'Ex: Agoè'}),
            'tarif_journalier': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-sm', 'placeholder': 'Ex: 10000'}),
        }