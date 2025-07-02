from django.shortcuts import render
from .models import Service

def services_list(request):
    services = Service.objects.all()  # Récupère tous les services
    return render(request, 'services/list.html', {'services':services})