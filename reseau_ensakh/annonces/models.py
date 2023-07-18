from django.db import models
from utilisateurs.models import Utilisateur

class Annonce(models.Model):
    titre = models.TextField(max_length=50)
    description = models.CharField(max_length=500)
    date_heure_de_creation = models.DateTimeField()
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)