from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Prestataire(models.Model):
    nom_complet = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='prestataires')
    telephone = models.CharField(max_length=20)
    quartier = models.CharField(max_length=100) # Ex: Agoè, Hedzranawoé, Bè...
    tarif_journalier = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_complet} - {self.categorie.nom}"