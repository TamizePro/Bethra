from django.shortcuts import render
from messagerie.models import Message
from django.contrib.auth.decorators import login_required


# id: Il s'agit de l'identifiant de l'expéditeur:
# l'utilisateur qui veut voir les messages qu'il a envoyé
@login_required
def liste_messages(request, id):
    messages = Message.objects.filter(expediteur__id=id)
    return render(request, 
                  'messagerie/messages.html', 
                  {'messages': messages})