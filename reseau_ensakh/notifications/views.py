from django.shortcuts import render
from notifications.models import Notification
from django.contrib.auth.decorators import login_required


@login_required
def notifications(request, id):
    # On récupère uniquement les notifications qui concerne l'utilisateur
    notifications_personnelles = Notification.objects.get(utilisateur__id=id)
    return render(request, 
                  'notifications/notifications.html', 
                  {'notifications': notifications_personnelles})