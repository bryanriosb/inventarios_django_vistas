from django.contrib import admin
from .models import *


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    pass

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ('ruc','nombre','direccion')
    list_edit = ('ruc','nombre','direccion')


class SalidaAdmin(admin.ModelAdmin):
    model=Salida

class DetalleSalidaAdmin(admin.ModelAdmin):
    model = DetalleSalida


admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Salida,SalidaAdmin)
admin.site.register(DetalleSalida,DetalleSalidaAdmin)



@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    model = Ingreso


@admin.register(DetalleIngreso)
class DetalleIngresoAdmin  (admin.ModelAdmin):
    model = DetalleIngreso
