import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class PuestoFilter(django_filters.FilterSet):
    class Meta:
        model = Puesto
        fields = { 
            'departamento':['exact'],
            'nombre_puesto':['icontains'],
            'numero_de_vacantes':['gte','lte'],
            'sueldo':['gte','lte'],
            'aptitudes_necesarias':['icontains'],
            'requisitos_puesto':['icontains'],
        }

class InformeFilter(django_filters.FilterSet):
    class Meta:
        model = InformeContable
        fields =  { 
            'id':['exact'],
            'fecha': ['gte','lte'],
        }

class BienFilter(django_filters.FilterSet):
    class Meta:
        model = Bien
        fields = { 
            'id':['exact'],
            'valor': ['gte','lte'],
            'nombre':['icontains'],
            'descripcion':['icontains'],
            'informe':['exact'],
        }

class VehiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Vehiculo
        fields = { 
            'matricula':['exact'],
            'numero_pasajeros': ['gte','lte'],
            'combustible':['icontains'],
            'trasmision':['icontains'],
            'tipo':['icontains'],
        }

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = { 
            'idProducto':['exact'],
            'cantidad': ['gte','lte'],
            'nombre':['icontains'],
            'precio': ['gte','lte'],
            'factura':['exact'],
        }

class ContieneFilter(django_filters.FilterSet):
    class Meta:
        model = Contiene
        fields = '__all__'


class ConsultaEmpleadoFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaEmpleado
        fields = '__all__'

class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = { 
            'dni':['exact'],
            'nombrecliente':['icontains'],
        }

class SolicitaAlquilerFilter(django_filters.FilterSet):
    class Meta:
        model = SolicitaAlquiler
        fields = { 
            'idAlquiler':['exact'],
            'ganancia': ['gte','lte'],
            'duracion': ['gte','lte'],
            'precio': ['gte','lte'],
            'cliente':['exact'],
        }

class ConsultaAlquilerFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaAlquiler
        fields = '__all__'

class BalanceFinancieroFilter(django_filters.FilterSet):
    class Meta:
        model = BalanceFinanciero
        fields = { 
            'idBalance':['exact'],
            'fecha_realizacion': ['gte','lte'],
            'total_gastos':['gte','lte'],
            'total_ingresos':['gte','lte'],
            'bienes_actuales':['gte','lte'],
            'deudas': ['gte','lte'],

        }

class ConsultaInformeContableFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaInformeContable
        fields = ['informe', 'balance']

class ConsultaFacturaFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaFactura
        fields = '__all__'

class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model = Factura
        fields = { 
            'id':['exact'],
            'fecha': ['gte','lte'],
            'total': ['gte','lte'],
            'proveedor':['icontains'],
        }

class EmpleadoTrabajaFilter(django_filters.FilterSet):
    class Meta:
        model = EmpleadoTrabaja
        fields = { 
            'idEmpleado':['exact'],
            'fecha_pago': ['gte','lte'],
            'fecha_alta': ['gte','lte'],
            'fecha_baja': ['gte','lte'],
            'cuenta_bancaria': ['exact'],
            'nombre':['icontains'],
            'apellidos':['icontains'],
            'nombre_puesto':['exact'],

        }


