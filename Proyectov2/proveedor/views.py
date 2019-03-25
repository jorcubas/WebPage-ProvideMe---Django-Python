from django.shortcuts import render, redirect
from .models import proveedor,provincia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import HttpResponse


@login_required
def home(request):
    context = {
        'proveedor' : proveedor.objects.select_related('provincia')
    }
    return render(request, 'proveedor/proveedor.html', context)

class proveedorListView(LoginRequiredMixin, ListView):
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

def reportes(request, id=None):
    template = 'proveedor/reporteProveedor.html'
    context = {
        'proveedor' : proveedor.objects.get(pk=id)
    }
    return render(request, template, context)