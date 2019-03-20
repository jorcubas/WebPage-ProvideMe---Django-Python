from django.urls import path
from .views import (
    proveedorListView,
    ProvDetailView,
    ProvCreateView,
    search
)
from . import views

urlpatterns = [
    path('', proveedorListView.as_view(), name = 'proveedor-proveedor'),
    path('proveedor/<int:pk>/', ProvDetailView.as_view(), name = 'proveedor-detail'),
    path('proveedor/new/', ProvCreateView.as_view(), name = 'proveedor-create'),
    path('results/', search, name="search")
]