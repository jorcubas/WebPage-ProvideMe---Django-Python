from django.shortcuts import render
from .models import proveedor
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'proveedor' : proveedor.objects.select_related('provincia')
    }
    return render(request, 'proveedor/proveedor.html', context)

