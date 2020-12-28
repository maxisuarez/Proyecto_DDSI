# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('Puestos', views.Puestos, name='Puestos'),
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

  path('vehiculos', views.vehiculos, name='vehiculos'),
  path('crearVehiculo', views.crearVehiculo, name='crearVehiculo'),
  path('editarVehiculo/<item_id>', views.editarVehiculo, name='editarVehiculo'),
  path('borrarVehiculo/<item_id>', views.borrarVehiculo, name='borrarVehiculo'),
  
  path('productos', views.productos, name='productos'),
  path('crearProducto', views.crearProducto, name='crearProducto'),
  path('editarProducto/<item_id>', views.editarProducto, name='editarProducto'),
  path('borrarProducto/<item_id>', views.borrarProducto, name='borrarProducto'),
  
   path('ConsultaEmpleados', views.ConsultaEmpleados, name='ConsultaEmpleados'),
  path('crearConsultaEmpleado', views.crearConsultaEmpleado, name='crearConsultaEmpleado'),
  path('editarConsultaEmpleado/<item_id>', views.editarConsultaEmpleado, name='editarConsultaEmpleado'),
  path('borrarConsultaEmpleado/<item_id>', views.borrarConsultaEmpleado, name='borrarConsultaEmpleado'),

  path('Clientes', views.Clientes, name='Clientes'),
  path('crearCliente', views.crearCliente, name='crearCliente'),
  path('editarCliente/<item_id>', views.editarCliente, name='editarCliente'),
  path('borrarCliente/<item_id>', views.borrarCliente, name='borrarCliente'),

  path('ConsultaAlquileres', views.ConsultaAlquileres, name='ConsultaAlquileres'),
  path('crearConsultaAlquiler', views.crearConsultaAlquiler, name='crearConsultaAlquiler'),
  path('editarConsultaAlquiler/<item_id>', views.editarConsultaAlquiler, name='editarConsultaAlquiler'),
  path('borrarConsultaAlquiler/<item_id>', views.borrarConsultaAlquiler, name='borrarConsultaAlquiler'),

  path('SolicitaAlquileres', views.SolicitaAlquileres, name='SolicitaAlquileres'),
  path('crearSolicitaAlquiler', views.crearSolicitaAlquiler, name='crearSolicitaAlquiler'),
  path('editarSolicitaAlquiler/<item_id>', views.editarSolicitaAlquiler, name='editarSolicitaAlquiler'),
  path('borrarSolicitaAlquiler/<item_id>', views.borrarSolicitaAlquiler, name='borrarSolicitaAlquiler'),
  
  path('contiene', views.contiene, name='contiene'),
  path('crearContiene', views.crearContiene, name='crearContiene'),
  path('editarContiene/<item_id>', views.editarContiene, name='editarContiene'),
  path('borrarContiene/<item_id>', views.borrarContiene, name='borrarContiene'),

  path('balanaceFinancieros', views.balanaceFinancieros, name='balanaceFinancieros'),
  path('crearBalanceFinanciero', views.crearBalanceFinanciero, name='crearBalanceFinanciero'),
  path('editarBalanceFinanciero/<item_id>', views.editarBalanceFinanciero, name='editarBalanceFinanciero'),
  path('borrarBalanceFinanciero/<item_id>', views.borrarBalanceFinanciero, name='borrarBalanceFinanciero'),

  path('ConsultaInformeContables', views.ConsultaInformeContables, name='ConsultaInformeContables'),
  path('crearConsultaInformeContable', views.crearConsultaInformeContable, name='crearConsultaInformeContable'),
  path('editarConsultaInformeContable/<item_id>', views.editarConsultaInformeContable, name='editarConsultaInformeContable'),
  path('borrarConsultaInformeContable/<item_id>', views.borrarConsultaInformeContable, name='borrarConsultaInformeContable'),

  path('ConsultaFacturas', views.ConsultaFacturas, name='ConsultaFacturas'),
  path('crearConsultaFactura', views.crearConsultaFactura, name='crearConsultaFactura'),
  path('editarConsultaFactura/<item_id>', views.editarConsultaFactura, name='editarConsultaFactura'),
  path('borrarConsultaFactura/<item_id>', views.borrarConsultaFactura, name='borrarConsultaFactura'),
]
