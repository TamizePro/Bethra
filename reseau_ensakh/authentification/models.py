from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        ELEVE = 'EL'
        ANCIEN_ELEVE = 'AE'
        PROFESSEUR = 'P'
        ENTREPRISE = 'EN'
        ADMINISTRATION = 'A' 
        #Pour un membre de l'administration de l'ENSA de Khouribga
    
    class Filiere(models.TextChoices):
        INFORMATIQUE_ET_INGENIEURIE_DES_DONNEES = 'IID'
        INGENIEURIE_DES_RESEAUX_INTELLIGENTS_ET_CYBERSECURITE = 'IRIC'
        GENIE_DES_PROCEDEES_ENERGIE_ENVIRONNEMENT = 'GPEE'
        GENIE_INFORMATIQUE = 'GI'
        GENIE_ELECTRIQUE = 'GE'
        AUCUNE = None
    
    class Niveau(models.TextChoices):
        PREMIERE_ANNEE = '1'
        DEUXIEME_ANNEE = '2'
        TROISIEME_ANNEE = '3'
        QUATRIEME_ANNEE = '4'
        CINQUIEME_ANNEE = '5'
        DOCTORANT = 'D'
        AUCUN = None
    
    role = models.fields.CharField(choices=Role.choices, max_length=2)
    filiere = models.fields.CharField(choices=Filiere.choices, null=True, max_length=4)
    poste = models.fields.CharField(null=True, blank=True, max_length=30)
    niveau = models.fields.CharField(choices=Niveau.choices, null=True, blank=True, max_length=30)
    connections = models.ManyToManyField('self', symmetrical=False)