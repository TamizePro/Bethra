from django import forms

class FormulaireConnexion(forms.Form):
    username = forms.CharField(max_length=150, label='Nom d’utilisateur')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Mot de passe')