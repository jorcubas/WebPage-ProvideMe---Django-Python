from django.shortcuts import render
from .models import proveedor

def home(request):
    context = {
        'proveedor' : proveedor.objects.select_related('provincia')
    }
    return render(request, 'proveedor/proveedor.html', context)

