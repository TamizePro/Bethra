from django.db import models
from authentification.models import Utilisateur

class Publication(models.Model):
    titre = models.TextField(max_length=20)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/publications', null=True, blank=True)
    video = models.FileField(upload_to='video/publications', null=True, blank=True)
    date_heure_de_creation = models.DateTimeField()
    utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)

class Commentaire(models.Model):
    texte = models.TextField(max_length=50)
    date_heure_de_creation = models.DateTimeField()
    publication = models.ForeignKey(Publication, null=True, on_delete=models.CASCADE)
    utilisateur = models.OneToOneField(Utilisateur,null=True, on_delete=models.CASCADE)