from django.shortcuts import render, redirect
from .models import proveedor,provincia, reporteProveedor, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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


#class proveedorDetailView(DetailView):
#    model = proveedor

def proveedorView(request, id = None):
    current_user = request.user
    try:
        reporteCheck = reporteProveedor.objects.get(Proveedor__id=id, Usuario__id=current_user.id)
    except reporteProveedor.DoesNotExist:
        reporteCheck = None

    if(reporteCheck == None):
        context = {
            'proveedor' : proveedor.objects.get(id = id),
            'reporteProveedor': 'holi',
            'usuario': User.objects.get(id = current_user.id),
        }
    else:
        context = {
            'proveedor' : proveedor.objects.get(id = id),
            'reporteProveedor': reporteProveedor.objects.get(Proveedor__id = id, Usuario__id = current_user.id),
            'usuario': User.objects.get(id = current_user.id),
        }
    return render(request, 'proveedor/proveedor_detail.html', context)

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

def reportadoProveedor(request, id=None):
    template = 'proveedor/reportadoProveedor.html'
    proveedorObj = proveedor.objects.get(id = id)
    current_user = request.user
    usuarioObj = User.objects.get(id = current_user.id)
    preportado = reporteProveedor(Proveedor = proveedorObj, Usuario = usuarioObj)
    preportado.save()
    context = {
        'proveedor' : proveedor.objects.get(pk=id)
    }
    return render(request, template, context)

