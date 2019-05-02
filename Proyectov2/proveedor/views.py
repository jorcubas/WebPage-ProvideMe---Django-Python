from django.shortcuts import render, redirect
from .models import proveedor, provincia, reporteProveedor, User, agregadoFavoritosProveedor, Comentario, Rating, ratings_prov
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .forms import FormComment
from django import forms
import datetime

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

def proveedorView(request, id):
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

def calificarProveedor(request, id = None):

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

            comment = Comentario(Proveedor_id=id, Usuario_id=current_user.id, fecha=str(datetime.date.today()), texto = Com)

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