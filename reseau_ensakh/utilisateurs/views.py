from django.shortcuts import render
from utilisateurs.models import Utilisateur

def mon_profil(request, id):
    profil_personnel = Utilisateur.objects.get(id=id)
    return render(request, 
                  'utilisateurs/profil_personnel.html', 
                  {'profil_personnel': profil_personnel})

# Il faut séparer les utilisateurs qui font partie du 
# réseau de l'utilisateur et ceux qui n'en font pas partie
def mon_reseau(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 
                  'utilisateurs/reseau.html', 
                  {'utilisateurs': utilisateurs})