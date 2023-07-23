from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publications.models import Publication



@login_required
def liste_publications(request):
    publications = Publication.objects.all()
    print(Publication.objects.count())
    return render(request, 
                  'publications/liste_publications.html', 
                  {'publications': publications})


@login_required
# Il faudrait retirer cette vue et le gabarit associé
def detail_publication(request, id):
    publication = Publication.objects.get(id=id)
    return render(request, 
                  'publications/detail_publication.html', 
                  {'publication': publication})