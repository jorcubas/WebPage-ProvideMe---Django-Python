from django.shortcuts import render
from .models import proveedor
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView

@login_required
def home(request):
    context = {
        'proveedor' : proveedor.objects.select_related('provincia')
    }
    return render(request, 'proveedor/proveedor.html', context)

class proveedorListView(ListView):
    model = proveedor
    template_name = 'proveedor/proveedor.html'
    context_object_name = 'proveedor'
    ordering = ['-nombre']


class proveedorDetailView(DetailView):
    model = proveedor

class proveedorCreateView(CreateView):
    model = proveedor
    fields=['nombre', 'correo', 'telefono', 'provincia']