"""
URL configuration for reseau_ensakh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from publications import views as vues_publications
from annonces import views as vues_annonces
from messagerie import views as vues_messagerie
from utilisateurs import views as vues_utilisateurs
from notifications import views as vues_notifications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publications/', vues_publications.liste_publications, name='liste_publications'),
    path('publications/<int:id>/', vues_publications.detail_publication, name='detail_publication'),
    path('annonces/', vues_annonces.liste_annonces, name='liste_annonces'),
    path('messagerie/<int:id>/', vues_messagerie.liste_messages, name='liste_messages'),
    path('mon_profil/<int:id>/', vues_utilisateurs.mon_profil, name='profil_personnel'),
    path('mon_reseau/', vues_utilisateurs.mon_reseau, name='reseau_personnel'),
    path('connexion/', vues_utilisateurs.connexion, name='connexion'),
    path('deconnexion/', vues_utilisateurs.deconnexion, name='deconnexion'),
    path('accueil/', vues_utilisateurs.page_d_accueil, name='accueil'),
    path('notifications/<int:id>/', vues_notifications.notifications, name='notifications'),
]
