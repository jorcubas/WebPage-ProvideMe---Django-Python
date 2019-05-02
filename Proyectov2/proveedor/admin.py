from django.contrib import admin
from .models import proveedor, reporteProveedor, agregadoFavoritosProveedor, Comentario

# Register your models here.
admin.site.register(proveedor)
admin.site.register(reporteProveedor)
admin.site.register(agregadoFavoritosProveedor)
admin.site.register(Comentario)
