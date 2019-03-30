from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    proveedorListView,
    proveedorView,
    proveedorCreateView,
    search,
    reportes,
    reportadoProveedor,
    agregadoFavorito,
    eliminadoFavorito
)
from . import views

urlpatterns = [
    path('', proveedorListView.as_view(), name = 'proveedor-proveedor'),
    path('proveedor/<id>/', proveedorView, name = 'proveedor-detail'),
    path('proveedor/new/', proveedorCreateView.as_view(), name = 'proveedor-create'),
    path('results/', search, name="search"),
    path('proveedor/reporteProveedor/<id>/', reportes, name = 'reportes'),
    path('proveedor/reportadoProveedor/<id>/', reportadoProveedor, name = 'reportadoProveedor'),
    path('proveedor/agregadoFavorito/<id>/', agregadoFavorito, name = 'agregadoFavorito'),
    path('proveedor/eliminadoFavorito/<id>/', eliminadoFavorito, name = 'eliminadoFavorito'),
]