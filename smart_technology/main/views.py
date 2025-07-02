from django.utils.translation import gettext
# Create your views here.

def accueil(request):
    return render(request, 'main/accueil.html')

def qui_sommes_nous(request):
    return render(request, 'main/qui_sommes_nous.html')

def services(request):
    return render(request, 'main/services.html')

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        contenu = f"""
NOM : {nom}
EMAIL : {email}
SUJET : {sujet}
MESSAGE :
{message}
        """

        send_mail(
            subject=f"[Contact Site SMART TECHNOLOGY] {sujet}",
            message=contenu,
            from_email='smartformulaire@gmail.com',  # ton adresse Gmail
            recipient_list=['smartformulaire@gmail.com'],  # le destinataire = toi
            fail_silently=False,
        )
        return render(request, 'main/confirmation.html')

    return render(request, 'main/contact.html')

