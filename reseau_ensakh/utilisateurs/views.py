from django.shortcuts import render, redirect
from utilisateurs.models import Utilisateur
from utilisateurs.forms import FormulaireConnexion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def mon_profil(request, id):
    profil_personnel = Utilisateur.objects.get(id=id)
    return render(request, 
                  'utilisateurs/profil_personnel.html', 
                  {'profil_personnel': profil_personnel})


# Il faut séparer les utilisateurs qui font partie du 
# réseau de l'utilisateur et ceux qui n'en font pas partie
@login_required
def mon_reseau(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 
                  'utilisateurs/reseau.html', 
                  {'utilisateurs': utilisateurs})


def page_d_accueil(request):
    return render(request, 
                  'utilisateurs/accueil.html')


def connexion(request):
    form = FormulaireConnexion()
    message = ''
    
    if request.method == 'POST':
        form = FormulaireConnexion(request.POST)
        
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            
            if user is not None:
                login(request, user)
                return redirect('liste_publications')
            else:
                message = 'Identifiants invalides.'

    return render(request, 
                  'utilisateurs/connexion.html', 
                  context={'form': form, 'message': message})


@login_required
def deconnexion(request):
    logout(request)
    return redirect('accueil')