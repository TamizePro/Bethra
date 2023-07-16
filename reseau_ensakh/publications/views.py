from django.shortcuts import render
from publications.models import Publication

def liste_publications(request):
    publications = Publication.objects.all()
    print(Publication.objects.count())
    return render(request, 
                  'publications/liste_publications.html', 
                  {'publications': publications})

def detail_publication(request, id):
    publication = Publication.objects.get(id=id)
    return render(request, 
                  'publications/detail_publication.html', 
                  {'publication': publication})