from django.db import models
from authentification.models import Utilisateur

class Message(models.Model):
    texte = models.CharField(max_length=1000, null=True, blank=True)
    fichier_audio = models.FileField(upload_to='audio/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    image = models.ImageField(upload_to='images/messagerie', null=True, blank=True)
    video = models.FileField(upload_to='video/messagerie', null=True, blank=True)
    
    #Indiquent que le message a été reçu ou vu
    recu = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    date_heure_de_creation = models.DateTimeField()
    
    #Ce message est la réponse à un autre message ou
    # Ce message repond à un autre message
    message = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='repondu_par')
    
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='envoye_par')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='recu_par')