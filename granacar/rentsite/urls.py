# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('puestos', views.puestos, name='puestos'),
  path('crearPuesto', views.crearPuesto, name='crearPuesto'),
  path('editarPuesto/<item_id>', views.editarPuesto, name='editarPuesto'),
  path('borrarPuesto/<item_id>', views.borrarPuesto, name='borrarPuesto'),
  path('empleados', views.empleados, name='empleados'),
  path('crearEmpleado', views.crearEmpleado, name='crearEmpleado'),
  path('editarEmpleado/<item_id>', views.editarEmpleado, name='editarEmpleado'),
  path('borrarEmpleado/<item_id>', views.borrarEmpleado, name='borrarEmpleado'),
  path('facturas', views.facturas, name='facturas'),
  path('crearFactura', views.crearFactura, name='crearFactura'),
  path('editarFactura/<item_id>', views.editarFactura, name='editarFactura'),
  path('borrarFactura/<item_id>', views.borrarFactura, name='borrarFactura'),
  path('bienes', views.bienes, name='bienes'),
  path('crearBien', views.crearBien, name='crearBien'),
  path('editarBien/<item_id>', views.editarBien, name='editarBien'),
  path('borrarBien/<item_id>', views.borrarBien, name='borrarBien'),
  path('informes', views.informes, name='informes'),
  path('crearInforme', views.crearInforme, name='crearInforme'),
  path('editarInforme/<item_id>', views.editarInforme, name='editarInforme'),
  path('borrarInforme/<item_id>', views.borrarInforme, name='borrarInforme'),
]
