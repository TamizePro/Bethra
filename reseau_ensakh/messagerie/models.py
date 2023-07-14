from django.db import models

class Message(models.Model):
    texte = models.CharField(max_length=1000, null=True, blank=True)
    fichier_audio = models.FileField(upload_to='audio/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    image = models.ImageField(upload_to='images/messagerie', null=True, blank=True)
    video = models.FileField(upload_to='video/messagerie', null=True, blank=True)
    date_heure_de_creation = models.DateTimeField()
    message = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='repondu_par')
    #Ce message est la réponse à un autre message ou
    # Ce message repond à un autre message