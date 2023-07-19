from django.db import models
from utilisateurs.models import Utilisateur

class Notification(models.Model):
    sujet = models.CharField(max_length=500)
    details = models.CharField(max_length=1000)
    date_heure_de_creation = models.DateTimeField(null=True, blank=True)
    
    # Il s'agit ici de l'utilisateur concerné par par la notification
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)