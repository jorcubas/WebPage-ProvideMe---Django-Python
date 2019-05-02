from django.shortcuts import render, redirect
from .models import proveedor, provincia, reporteProveedor, User, agregadoFavoritosProveedor, Comentario, Rating, ratings_prov
from .models import proveedor,provincia, reporteProveedor, User, agregadoFavoritosProveedor,movimientos_pagina
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .forms import FormComment
from django import forms
from datetime import datetime,timedelta, date



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
    elif id == '2':
        ordering = proveedor.objects.select_related('provincia').order_by('calificacion')
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
    try:
        reporteIsCommented = Comentario.objects.get(Proveedor__id=id, Usuario__id=current_user.id)
    except Comentario.DoesNotExist:
        reporteIsCommented = 'sinComentario'
    isSuperUser = current_user.is_staff and current_user.is_superuser
    context = {
        'proveedor' : proveedor.objects.get(id = id),
        'reporteProveedor': reporteCheck,
        'usuario': User.objects.get(id = current_user.id),
        'agregadoFavorito': reporteCheckFavorito,
        'isComentario' : reporteIsCommented,
        'isSuperUser' : isSuperUser
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
            results = proveedor.objects.filter(calificacion__gte = 5)
    elif id == '2':
            results = proveedor.objects.filter(calificacion__gte = 7)
    elif id == '3':
            results = proveedor.objects.filter(calificacion = 10)
    elif id == '4':
            results = proveedor.objects.filter(provincia_id = 1)
    elif id == '5':
            results = proveedor.objects.filter(Q(provincia_id = 2))
    elif id == '6':
            results = proveedor.objects.filter(Q(provincia_id = 3))
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



def calificarProveedor(request, id=None):
    if request.method == 'POST':
        form = FormComment(request.POST)
    form = FormComment()
    context = {
        'form': form,
        'proveedor' : id
    }
    return render(request, 'proveedor/comentarioForm.html', context)


def formComentario(request):
    template = 'proveedor/comentarioForm.html'
    form = FormComment()
    {'form': form}
    return render(request, template)

def respuesta(request, id = None):
    if request.method == 'POST':

        form = FormComment(request.POST)
        if form.is_valid():

            current_user = request.user
            usuarioObj = User.objects.get(id=current_user.id)

            Com = form.cleaned_data['Comentario']

            comment = Comentario(Proveedor_id=id, Usuario_id=current_user.id, fecha=str(date.today()), texto = Com)

            comment.save()

            Calidad = form.cleaned_data['Calidad']
            Precio = form.cleaned_data['Precio']
            Servicio = form.cleaned_data['Servicio']
            Trato = form.cleaned_data['Trato']

            rat = Rating(Proveedor_id=id, Usuario_id=current_user.id, promedio=(int(Calidad)+int(Precio)+int(Servicio)+int(Trato))/4)

            rat.save()

            current_rating = Rating.objects.get(Proveedor_id = id, Usuario_id=current_user.id)
            current_comment =  Comentario.objects.get(Proveedor_id=id, Usuario_id=current_user.id)



            rats_prov = ratings_prov(rating_id=current_rating.id, comentario_id=current_comment.id, tipo='Calidad',
                                     calificacion=Calidad)

            rats_prov.save()

            rats_prov = ratings_prov(rating_id=current_rating.id, comentario_id=current_comment.id, tipo='Precio',
                                     calificacion=Precio)

            rats_prov.save()

            rats_prov = ratings_prov(rating_id=current_rating.id, comentario_id=current_comment.id, tipo='Servicio',
                                     calificacion=Servicio)

            rats_prov.save()

            rats_prov = ratings_prov(rating_id=current_rating.id, comentario_id=current_comment.id, tipo='Trato',
                                     calificacion=Trato)

            rats_prov.save()

            prom_rat = Rating.objects.all().filter(Proveedor_id=id)
            suma = 0
            cont = 0

            for item in prom_rat:
                suma += item.promedio
                cont += 1

            newProv= proveedor.objects.get(id=id)
            newProv.calificacion = suma/cont
            newProv.save()



    return render(request, 'proveedor/mensajeRespuesta.html', {'proveedor': id})


@login_required
def comment_approve(request, pk, id= None):
    comment = get_object_or_404(Comentario, pk=pk)
    comment.approve()
    context = {
        'proveedor' : id,
        'aprobado' : True
    }
    return render(request, 'proveedor/respuestaComment.html', context)

@login_required
def comment_remove(request, pk, id=None):
    comment = get_object_or_404(Comentario, pk=pk)
    comment.delete()
    context = {
        'proveedor': id,
        'aprobado': False
    }
    return render('proveedor/respuestaComment.html', context)