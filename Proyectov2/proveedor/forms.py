from django import forms

from .models import proveedor,provincia

class FormCrearProveedor(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre', 'correo', 'telefono']

