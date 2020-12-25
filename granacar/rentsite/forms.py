from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from datetime import datetime
from .models import *

class PuestoForm(ModelForm):
    class Meta:
        model = Puesto
        fields = ['nombre_puesto', 'departamento', 'numero_de_vacantes', 'aptitudes_necesarias', 'requisitos_puesto', 'sueldo']
        
    def registrar(self):
        nuevo_item = Puesto(nombre_puesto=self.data['nombre_puesto'],
                        departamento=self.data['departamento'],
                        numero_de_vacantes=int(self.data['numero_de_vacantes']),
                        aptitudes_necesarias=self.data['aptitudes_necesarias'],
                        requisitos_puesto=self.data['requisitos_puesto'],
                        sueldo=self.data['sueldo'])
        nuevo_item.save()
        return 'Registro exitoso'


class EmpleadoForm(ModelForm):
    class Meta:
        model = EmpleadoTrabaja
        fields = ['idEmpleado', 'nombre', 'apellidos', 'nombre_puesto', 'cuenta_bancaria', 'fecha_pago', 'fecha_alta', 'fecha_baja']
        

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




