from django.contrib import admin
from .models import Proveedor, Producto, Factura, FacturaDetalle, Cliente

class FacturaDetalleInline(admin.TabularInline):
    model = FacturaDetalle
    extra = 1  # Número de filas vacías para agregar productos en la factura

class FacturaAdmin(admin.ModelAdmin):
    inlines = [FacturaDetalleInline]
    list_display = ('id', 'proveedor', 'cliente', 'producto', 'cantidad', 'fecha_creacion', 'pendiente')  # Agregado campo 'pendiente'
    list_filter = ['fecha_creacion', 'proveedor', 'cliente', 'pendiente']  # Agregado filtro por 'pendiente'
    search_fields = ['proveedor__nombre', 'cliente__nombre', 'producto__nombre']
    list_editable = ['pendiente']  # Permitir editar el estado 'pendiente' directamente desde la lista

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_cliente', 'precio_Publico', 'precio_compra')
    list_filter = ['categoria']
    search_fields = ['nombre']


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    filter_horizontal = ('productos_ofrecidos',)

admin.site.register(FacturaDetalle)
admin.site.register(Cliente)
admin.site.register(Proveedor, ProveedorAdmin)  # Usar ProveedorAdmin para el modelo Proveedor
admin.site.register(Producto, ProductoAdmin)  # Usar ProductoAdmin para el modelo Producto
admin.site.register(Factura, FacturaAdmin)
