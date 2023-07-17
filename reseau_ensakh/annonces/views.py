from django.shortcuts import render
from annonces.models import Annonce

def liste_annonces(request):
    annonces = Annonce.objects.all()
    return render(request, 
                  'annonces/liste_annonces.html', 
                  {'annonces': annonces})