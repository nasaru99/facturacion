from django.shortcuts import render
from .models import Proveedor, Producto, Factura, FacturaDetalle, Cliente
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from .forms import FacturaForm, FacturaDetalleFormSet
from django.shortcuts import render, get_object_or_404

def inicio(request):
    return render(request, 'inicio.html')


def clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
         
        cliente = Cliente(nombre=nombre, )
        cliente.save()
    
    # Recupera todos los clientes
    clientes = Cliente.objects.all().prefetch_related('factura_set')

    # Pasa los clientes al contexto del template
    context = {
        'clientes': clientes
    }

    # Renderiza el template con el contexto
    return render(request, 'clientes.html', context)
 

def provedores(request):
# Recuperar proveedores por categoría
    proveedores_res = Proveedor.objects.filter(productos_ofrecidos__categoria='res').distinct()
    proveedores_pollo = Proveedor.objects.filter(productos_ofrecidos__categoria='pollo').distinct()
    proveedores_cerdo = Proveedor.objects.filter(productos_ofrecidos__categoria='cerdo').distinct()
    proveedores_embutido = Proveedor.objects.filter(productos_ofrecidos__categoria='embutido').distinct()

    # Aquí asumo que tienes un campo 'pendiente' en el modelo Factura y que 'proveedor' es una relación ForeignKey en Factura
    for proveedor in proveedores_res:
        proveedor.facturas_pendientes = Factura.objects.filter(proveedor=proveedor, pendiente=True)

    for proveedor in proveedores_pollo:
        proveedor.facturas_pendientes = Factura.objects.filter(proveedor=proveedor, pendiente=True)

    for proveedor in proveedores_cerdo:
        proveedor.facturas_pendientes = Factura.objects.filter(proveedor=proveedor, pendiente=True)

    for proveedor in proveedores_embutido:
        proveedor.facturas_pendientes = Factura.objects.filter(proveedor=proveedor, pendiente=True)

    context = {
        'proveedores_res': proveedores_res,
        'proveedores_pollo': proveedores_pollo,
        'proveedores_cerdo': proveedores_cerdo,
        'proveedores_embutido': proveedores_embutido,
    }

    return render(request, 'provedores.html', context)


def detalle_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    detalles_factura = FacturaDetalle.objects.filter(factura=factura)

    detalles_con_costo = []
    for detalle in detalles_factura:
        costo = float(detalle.cantidad) * float(detalle.producto.precio_cliente)
        detalles_con_costo.append({
            'detalle': detalle,
            'costo': costo
        })

    context = {
        'factura': factura,
        'detalles_con_costo': detalles_con_costo
    }

    return render(request, 'detalle_factura.html', context)


def crear_factura(request, cliente_id, proveedor):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        detalle_formset = FacturaDetalleFormSet(request.POST, prefix='detalles')

        if factura_form.is_valid() and detalle_formset.is_valid():
            factura = factura_form.save(commit=False)
            factura.proveedor = Proveedor.objects.get(nombre="Tramo")  # Proveedor por defecto
            factura.relacion_id = 1
            factura.cliente = cliente_id=int
            factura.save()
            detalles = detalle_formset.save(commit=False)
            for detalle in detalles:
                detalle.factura = factura
                detalle.save()
            return redirect('clientes')
    else:
        factura_form = FacturaForm()
        detalle_formset = FacturaDetalleFormSet(prefix='detalles')

    context = {
        'factura_form': factura_form,
        'detalle_formset': detalle_formset
    }

    return render(request, 'crear_factura.html', context)

def productos(request):
   # Obtener los productos de cada categoría
    productos_res = Producto.objects.filter(categoria='Res')
    productos_pollo = Producto.objects.filter(categoria='Pollo')
    productos_cerdo = Producto.objects.filter(categoria='Cerdo')
    productos_embutido = Producto.objects.filter(categoria='Embutido')

    # Pasar los productos al contexto
    context = {
        'productos_res': productos_res,
        'productos_pollo': productos_pollo,
        'productos_cerdo': productos_cerdo,
        'productos_embutido': productos_embutido,
    }

    return render(request, 'productos.html', context)

def facturas(request):
    return render(request, 'factura.html')
# Create your views here.
