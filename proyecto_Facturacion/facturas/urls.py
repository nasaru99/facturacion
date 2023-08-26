from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('provedores', views.provedores, name='provedores'),
    path('clientes', views.clientes, name='clientes'),
    path('productos', views.productos, name='productos'),
    path('facturas', views.facturas, name='facturas'),
    path('factura/<int:factura_id>/', views.detalle_factura, name='detalle_factura'),
     path('crear_factura/<int:cliente_id>/<str:proveedor>/', views.crear_factura, name='crear_factura'),


]