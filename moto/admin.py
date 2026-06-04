# moto/admin.py

from django.contrib import admin
from moto.models import Cliente, Vendedor, Moto, Venta, DetalleVenta


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre', 'apellido', 'cedula', 'telefono']
    search_fields = ['nombre', 'apellido', 'cedula', 'telefono']


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre', 'apellido', 'cedula', 'telefono']
    search_fields = ['nombre', 'apellido', 'cedula', 'telefono']


@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display  = ['id', 'marca', 'modelo', 'anio', 'color', 'precio', 'stock']
    search_fields = ['marca', 'modelo', 'color']
    list_filter   = ['marca', 'anio', 'color']
    list_editable = ['precio', 'stock']


class DetalleVentaInline(admin.TabularInline):
    model  = DetalleVenta
    extra  = 0
    fields = ['moto', 'cantidad', 'precio_unitario']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'cliente', 'vendedor', 'total']
    search_fields = [
        'cliente__nombre',
        'cliente__apellido',
        'cliente__cedula',
        'vendedor__nombre',
        'vendedor__apellido',
        'vendedor__cedula',
    ]
    inlines = [DetalleVentaInline]


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'venta', 'moto', 'cantidad', 'precio_unitario']
    list_filter   = ['moto']
    search_fields = ['moto__marca', 'moto__modelo', 'venta__id']