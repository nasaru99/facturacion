from django.db import models

class Proveedor(models.Model):
    PRODUCTO_CHOICES = [
        ('res', 'Res'),
        ('pollo', 'Pollo'),
        ('cerdo', 'Cerdo'),
        ('embutido', 'Embutido'),
    ]
    nombre = models.CharField(max_length=100)
    productos_ofrecidos = models.ManyToManyField('Producto', related_name='proveedores')


    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    PRODUCTO_CHOICES = [
        ('res', 'Res'),
        ('pollo', 'Pollo'),
        ('cerdo', 'Cerdo'),
        ('embutido', 'Embutido'),
    ]
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=10, choices=PRODUCTO_CHOICES)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True, related_name='productos_relacionados')
    precio_cliente = models.DecimalField(max_digits=10, decimal_places=2)
    precio_Publico = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    es_proveedor = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=True)  # Campo para facturas pendientes
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    relacion_id = models.PositiveIntegerField()

    def __str__(self):
        return f"Factura {self.id} - {self.fecha_creacion.strftime('%Y-%m-%d')}"

class FacturaDetalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
