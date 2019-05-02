from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import  proveedor, Comentario, Rating

from .models import proveedor,provincia

class FormCrearProveedor(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre', 'correo', 'telefono']

class FormComment(forms.Form):
    Calidad = forms.ChoiceField(label="Calificación de Calidad", choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])
    Precio = forms.ChoiceField(label="Calificación de Calidad", choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])
    Servicio = forms.ChoiceField(label="Calificación de Calidad", choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])
    Trato = forms.ChoiceField(label="Calificación de Calidad", choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])
    Comentario = forms.CharField(label="Ingrese un comentario sobre el proveedor", widget=forms.Textarea)
