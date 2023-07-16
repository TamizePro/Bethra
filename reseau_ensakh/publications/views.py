from django.shortcuts import render
from publications.models import Publication

def liste_publications(request):
    publications = Publication.objects.all()
    print(Publication.objects.count())
    return render(request, 
                  'publications/liste_publications.html', 
                  {'publications': publications})
