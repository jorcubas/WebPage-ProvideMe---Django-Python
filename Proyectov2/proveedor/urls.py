from django.urls import path
from .views import (
    proveedorListView,
    proveedorDetailView,
    proveedorCreateView,
    search
)
from . import views

urlpatterns = [
    path('', proveedorListView.as_view(), name = 'proveedor-proveedor'),
    path('proveedor/<int:pk>/', proveedorDetailView.as_view(), name = 'proveedor-detail'),
    path('proveedor/new/', proveedorCreateView.as_view(), name = 'proveedor-create'),
    path('results/', search, name="search"),
]