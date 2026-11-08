from django.contrib import admin
from .models import Categorie, Prestataire

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

@admin.register(Prestataire)
class PrestataireAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'categorie', 'quartier', 'tarif_journalier', 'disponible')
    list_filter = ('disponible', 'categorie', 'quartier')
    search_fields = ('nom_complet', 'quartier', 'telephone')
