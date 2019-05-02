from django.shortcuts import render, redirect
from .models import proveedor,provincia, reporteProveedor, User, agregadoFavoritosProveedor,movimientos_pagina
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from datetime import datetime,timedelta



@login_required
def firstLogin(request, id= None):
    current_user = request.user
    ordering = proveedor.objects.select_related('provincia')
    context = {
        'proveedor' : ordering,
        'usuario': User.objects.get(id = current_user.id),
    }
    usuarioObj = User.objects.get(id=current_user.id)
    guardadoMovimiento = movimientos_pagina(UsuarioMovimiento = usuarioObj, TipoMovimiento = 'Ingreso Pagina',
                                            FechaMovimiento = datetime.today(), HoraMovimiento = datetime.now())
    guardadoMovimiento.save()
    return render(request, 'proveedor/proveedor.html', context)


@login_required
def home(request, id= None):
    current_user = request.user
    if id == '1':
        ordering = proveedor.objects.select_related('provincia').order_by('nombre')
    else:
        ordering = proveedor.objects.select_related('provincia')
    context = {
        'proveedor' : ordering,
        'usuario': User.objects.get(id = current_user.id),
    }
    return render(request, 'proveedor/proveedor.html', context)

class proveedorListView(LoginRequiredMixin, ListView):
        model = proveedor
        template_name = 'proveedor/proveedor.html'
        context_object_name = 'proveedor'
        if id == 1:
            ordering = ['-nombre']
        else:
            ordering = ['nombre']


#class proveedorDetailView(DetailView):
#    model = proveedor

class proveedorCreateView(CreateView):
    model = proveedor
    fields=['nombre', 'correo', 'telefono', 'provincia']


def proveedorVista(request, id = None):
    current_user = request.user
    try:
        reporteCheck = reporteProveedor.objects.get(Proveedor__id=id, Usuario__id=current_user.id)
    except reporteProveedor.DoesNotExist:
        reporteCheck = 'sinReportar'

    try:
        reporteCheckFavorito = agregadoFavoritosProveedor.objects.get(Proveedor__id=id, Usuario__id=current_user.id)
    except agregadoFavoritosProveedor.DoesNotExist:
        reporteCheckFavorito = 'sinFavorito'

    context = {
        'proveedor' : proveedor.objects.get(id = id),
        'reporteProveedor': reporteCheck,
        'usuario': User.objects.get(id = current_user.id),
        'agregadoFavorito': reporteCheckFavorito,
    }

    return render(request, 'proveedor/proveedor_detail.html', context)



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

def filtro(request,id):
    template = 'proveedor/proveedor.html'
    #query = request.GET.get('q')
    #if query:
    if id == '1':
            results = proveedor.objects.all() # Muestra todos los proveedores por el momento, dado que no hay puntos
    elif id == '2':
            results = proveedor.objects.all() # Muestra todos los proveedores por el momento, dado que no hay puntos
    elif id == '3':
            results = proveedor.objects.all() # Muestra todos los proveedores por el momento, dado que no hay puntos
    elif id == '4':
            results = proveedor.objects.filter(provincia__id = 1)
    elif id == '5':
            results = proveedor.objects.filter(Q(provincia_id = 3))
    elif id == '6':
            results = proveedor.objects.filter(Q(provincia_id = 2))
    elif id == '7':
            results = proveedor.objects.filter(Q(provincia_id = 4))
    elif id == '8':
            results = proveedor.objects.filter(Q(provincia_id = 5))
    elif id == '9':
            results = proveedor.objects.filter(Q(provincia_id = 6))
    elif id == '10':
            results = proveedor.objects.filter(Q(provincia_id = 7))
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

def agregadoFavorito(request, id = None):
    template = 'proveedor/agregado_Favorito.html'
    proveedorObj = proveedor.objects.get(id=id)
    current_user = request.user
    usuarioObj = User.objects.get(id=current_user.id)
    agregadoaFavorito = agregadoFavoritosProveedor(Proveedor=proveedorObj, Usuario=usuarioObj)
    agregadoaFavorito.save()
    context = {
        'proveedor' : proveedor.objects.get(pk=id)
    }
    return render(request, template, context)

def eliminadoFavorito(request, id = None):
    template = 'proveedor/eliminado_Favorito.html'
    proveedorObj = proveedor.objects.get(id=id)
    current_user = request.user
    usuarioObj = User.objects.get(id=current_user.id)
    agregadoaFavorito = agregadoFavoritosProveedor.objects.get(Proveedor=proveedorObj, Usuario=usuarioObj)
    agregadoaFavorito.delete()
    context = {
        'proveedor' : proveedor.objects.get(pk=id)
    }
    return render(request, template, context)

def favoritosUsuario(request):
    template = 'proveedor/favoritosUsuario.html'
    current_user = request.user
    listaProveedores = agregadoFavoritosProveedor.objects.get(Usuario__id = current_user.id)
    listaFavoritos = listaProveedores.Proveedor
    context = {
        'proveedor' : listaFavoritos,
    }
    return render(request, template, context)

def envioCorreo(request, id = None):
    template = 'proveedor/envioCorreo.html'
    nombre_proveedor = proveedor.objects.get(pk=id)
    current_user = request.user
    usuarioObj = User.objects.get(id=current_user.id)
    emailUser = usuarioObj.email
    send_mail('Información de Contacto de ' + nombre_proveedor.nombre + ": ",
              'A Continuación Se Presenta la Información de Contacto de ' + nombre_proveedor.nombre + ": \n" + '\n' +
              'e-mail: ' + nombre_proveedor.correo + '\n' + '\n' +
              'telefono: ' + str(nombre_proveedor.telefono) + '\n' + '\n' +
              'provincia: ' + nombre_proveedor.provincia.nombre,
              'proveedoressho@gmail.com',
              [emailUser],
              fail_silently=False)
    context = {
        'proveedor' : proveedor.objects.get(pk=id)
    }
    return render(request, template, context)

def trafico(request):
    template = 'proveedor/trafico.html'
    return render(request, template)

def envíoTraficoIngresos(request):
    last_month = datetime.today() - timedelta(days=30)
    items = movimientos_pagina.objects.filter(FechaMovimiento__gte=last_month)
    usuario2 = request.user
    text = ""
    for movimiento in items:
        usuario = movimiento.UsuarioMovimiento.username
        tipoMovimiento = movimiento.TipoMovimiento
        fecha = str(movimiento.FechaMovimiento)
        hora = str(movimiento.HoraMovimiento)
        text += usuario + "\n" + tipoMovimiento + "\n" + fecha + "\n" + hora + "\n" + "\n" + "\n"
    send_mail('Trafico de Ingresos a Página Web ',
              text,
              'proveedoressho@gmail.com',
              [usuario2.email],
              fail_silently=False)
    template = 'proveedor/trafico_enviado.html'
    return render(request, template)






