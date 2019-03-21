from django.shortcuts import render
from .models import proveedor
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

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


def search(request):
    template = 'proveedor/proveedor.html'
    query = request.GET.get('q')
    if query:
        results = proveedor.objects.filter(Q(nombre__icontains=query))
    else:
        results = proveedor.objects.all()
    context = {
        'proveedor': results
    }
    return render(request, template, context)