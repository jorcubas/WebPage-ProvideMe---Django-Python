from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    proveedorListView,
    proveedorView,
    proveedorCreateView,
    search,
    filtro,
    reportes,
    reportadoProveedor,
    agregadoFavorito,
    eliminadoFavorito,
    home,
    favoritosUsuario,
    envioCorreo,
    calificarProveedor,
    formComentario,
    respuesta
)
from . import views
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('', home, name = 'proveedor-proveedor'),
    path('home/<id>/', home, name = 'proveedor-proveedor-orden'),
    path('home/filtro/<id>/', filtro, name = 'proveedor-proveedor-filtro'),
    path('proveedor/<id>/', proveedorView, name = 'proveedor-detail'),
    path('new/', proveedorCreateView.as_view(), name = 'proveedor-create'),
    path('results/', search, name="search"),
    path('proveedor/reporteProveedor/<id>/', reportes, name = 'reportes'),
    path('proveedor/reportadoProveedor/<id>/', reportadoProveedor, name = 'reportadoProveedor'),
    path('proveedor/agregadoFavorito/<id>/', agregadoFavorito, name = 'agregadoFavorito'),
    path('proveedor/eliminadoFavorito/<id>/', eliminadoFavorito, name = 'eliminadoFavorito'),
    path('proveedor/envioCorreo/<id>/', envioCorreo, name = 'envioCorreo'),
    path('favoritos/', favoritosUsuario, name = 'favoritosUsuario'),
    path('comentario/<id>/', calificarProveedor ,name='calificar-prov'),
    path('calificacion/<id>/', respuesta, name='resp')
]