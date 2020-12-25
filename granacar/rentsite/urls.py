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
]
