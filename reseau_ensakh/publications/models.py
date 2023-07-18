from django.db import models
from utilisateurs.models import Utilisateur

class Publication(models.Model):
    titre = models.TextField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/publications', null=True, blank=True)
    video = models.FileField(upload_to='video/publications', null=True, blank=True)
    date_heure_de_creation = models.DateTimeField()
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Commentaire(models.Model):
    texte = models.TextField(max_length=50)
    date_heure_de_creation = models.DateTimeField()
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    auteur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)