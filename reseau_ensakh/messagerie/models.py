from django.db import models
from utilisateurs.models import Utilisateur

# Il faut implémenter le cryptage des données des messages:
# Le texte et les fichiers

class Message(models.Model):
    # Contenu du message:
    # peut etre du texte, un message vocal ou tout autre fichier
    texte = models.CharField(max_length=1000, null=True, blank=True)
    fichier = models.FileField(upload_to='fichiers/messsagerie/', null=True, blank=True)
    
    # Indiquent que le message a été reçu ou vu
    vu = models.BooleanField(default=False)
    
    # La date de création du message
    date_heure_de_creation = models.DateTimeField()
    
    # Ce message est la réponse à un autre message ou
    # Ce message repond à un autre message
    message = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='repondu_par')
    
    # Expediteur: celui qui envoi le message
    # Destinataire: celui qui doit recevoir le message
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='envoye_par')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='recu_par')