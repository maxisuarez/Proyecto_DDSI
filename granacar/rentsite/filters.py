import django_filters

from .models import *

class PuestoFilter(django_filters.FilterSet):
    class Meta:
        model = Puesto
        fields = '__all__'

class InformeFilter(django_filters.FilterSet):
    class Meta:
        model = InformeContable
        fields = '__all__'

class BienFilter(django_filters.FilterSet):
    class Meta:
        model = Bien
        fields = '__all__'

class VehiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = '__all__'

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
        fields = '__all__'

class SolicitaAlquilerFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConsultaAlquilerFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaAlquiler
        fields = '__all__'

class BalanceFinancieroFilter(django_filters.FilterSet):
    class Meta:
        model = BalanceFinanciero
        fields = '__all__'

class ConsultaInformeContableFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaInformeContable
        fields = '__all__'

class ConsultaFacturaFilter(django_filters.FilterSet):
    class Meta:
        model = ConsultaFactura
        fields = '__all__'

class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model = Factura
        fields = '__all__'

class EmpleadoTrabajaFilter(django_filters.FilterSet):
    class Meta:
        model = EmpleadoTrabaja
        fields = '__all__'


