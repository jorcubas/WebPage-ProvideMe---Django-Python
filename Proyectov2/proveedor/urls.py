from django.urls import path
from .views import proveedorListView, proveedorDetailView
from . import views

urlpatterns = [
    path('', proveedorListView.as_view(), name = 'proveedor-proveedor'),
    path('proveedor/<int:pk>/', proveedorDetailView.as_view(), name = 'proveedor-detail'),
]