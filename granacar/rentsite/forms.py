from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from datetime import datetime
from .models import *

class PuestoForm(ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'


class EmpleadoForm(ModelForm):
    class Meta:
        model = EmpleadoTrabaja
        fields = '__all__'

'''
    fecha_pago = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2021)))
    fecha_alta = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2021)))
    fecha_baja = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2021)))

    def registrar(self):
        fechaPago = datetime(int(self.data['fecha_pago_year']),
                        int(self.data['fecha_pago_month']),
                        int(self.data['fecha_pago_day']))
        fechaAlta = datetime(int(self.data['fecha_alta_year']),
                        int(self.data['fecha_alta_month']),
                        int(self.data['fecha_alta_day']))
        fechaBaja = datetime(int(self.data['fecha_baja_year']),
                        int(self.data['fecha_baja_month']),
                        int(self.data['fecha_baja_day']))
        nuevo_empleado = EmpleadoTrabaja(idEmpleado = self.data['idEmpleado'],
                        nombre = self.data['nombre'],
                        apellidos = self.data['apellidos'],
                        nombre_puesto = self.instance.nombre_puesto,
                        cuenta_bancaria = self.data['cuenta_bancaria'],
                        fecha_pago = fechaPago,
                        fecha_alta = fechaAlta,
                        fecha_baja = fechaBaja)
        nuevo_empleado.save()
        return 'Registro exitoso'
'''


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        #exclude = ('id',)


    #fecha = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2021)))
    #id=forms.CharField(max_length=5,min_length=5)


class InformeForm(ModelForm):
    class Meta:
        model = InformeContable
        fields = '__all__'

class BienForm(ModelForm):
    class Meta:
        model = Bien
        fields = '__all__'

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ContieneForm(ModelForm):
    class Meta:
        model = Contiene
        fields = '__all__'


class ConsultaEmpleadoForm(ModelForm):
    class Meta:
        model = ConsultaEmpleado
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class SolicitaAlquilerForm(ModelForm):
    class Meta:
        model = SolicitaAlquiler
        fields = '__all__'

class ConsultaAlquilerForm(ModelForm):
    class Meta:
        model = ConsultaAlquiler
        fields = '__all__'

class BalanceFinancieroForm(ModelForm):
    class Meta:
        model = BalanceFinanciero
        fields = '__all__'

class ConsultaInformeContableForm(ModelForm):
    class Meta:
        model = ConsultaInformeContable
        fields = '__all__'

class ConsultaFacturaForm(ModelForm):
    class Meta:
        model = ConsultaFactura
        fields = '__all__'
