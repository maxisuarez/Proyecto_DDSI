# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, redirect
from .forms import *

def index(request):
    return render(request,'base.html')

def crearPuesto(request):
    if request.method == 'POST':
        register_form = PuestoForm(request.POST)
        if register_form.is_valid():
            success = register_form.registrar()
            return redirect(puestos)
    else:
        nuevoPuesto = PuestoForm()
        return render(request,'nuevo_puesto.html', {'register_form': nuevoPuesto})

def puestos(request):
    items = Puesto.objects.all()  # Aquí van la las variables para la plantilla
    return render(request,'lista_puestos.html', {'items': items })

def editarPuesto(request, item_id):
    instancia = Puesto.objects.get(pk=item_id)

    form = PuestoForm(instance=instancia)

    if request.method == 'POST':
        form = Puesto(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
        return redirect(puestos)

    return render(request,'editar_puesto.html', {'register_form': form, 'item_id':item_id})

def borrarPuesto(request, item_id):
    instance = Puesto.objects.get(pk=item_id)
    instance.delete()
    return redirect(puestos)

def crearEmpleado(request):
    if request.method == 'POST':
        register_form = EmpleadoForm(request.POST)
        if register_form.is_valid():
            success = register_form.registrar()
            return redirect(empleados)
    else:
        nuevoEmpleado = EmpleadoForm()
        return render(request,'nuevo_empleado.html', {'register_form': nuevoEmpleado})

def empleados(request):
    items = EmpleadoTrabaja.objects.all()  # Aquí van la las variables para la plantilla
    return render(request,'lista_empleados.html', {'items': items })

def editarEmpleado(request, item_id):
    instancia = EmpleadoTrabaja.objects.get(pk=item_id)

    form = EmpleadoForm(instance=instancia)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
        return redirect(empleados)

    return render(request,'editar_empleado.html', {'register_form': form, 'item_id':item_id})

def borrarEmpleado(request, item_id):
    instance = EmpleadoTrabaja.objects.get(pk=item_id)
    instance.delete()
    return redirect(empleados)

def crearFactura(request):
    error=None
    if request.method == 'POST':
        register_form = FacturaForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('facturas')
        else:
            error=register_form.errors
    else:
        register_form = FacturaForm()
    return render(request,'nueva_factura.html', {'form': register_form,'error': error})

def facturas(request):
    items = Factura.objects.all().order_by('fecha')
    return render(request,'lista_facturas.html', {'items': items })

def editarFactura(request, item_id):
    error=None
    instancia = Factura.objects.get(pk=item_id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('facturas')
        else:
            error=form.errors
    else:
        form = FacturaForm(instance=instancia)

    return render(request,'editar_factura.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarFactura(request, item_id):
    instance = Factura.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('facturas')
    return render(request,'borrar_factura.html',{'instance': instance})


def crearBien(request):
    error=None
    if request.method == 'POST':
        register_form = BienForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('bienes')
        else:
            error=register_form.errors
    else:
        register_form = BienForm()
    return render(request,'nuevo_bien.html', {'form': register_form,'error': error})

def bienes(request):
    items = Bien.objects.all().order_by('nombre')
    return render(request,'lista_bienes.html', {'items': items })

def editarBien(request, item_id):
    error=None
    instancia = Bien.objects.get(pk=item_id)
    if request.method == 'POST':
        form = BienForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('bienes')
        else:
            error=form.errors
    else:
        form = BienForm(instance=instancia)

    return render(request,'editar_bien.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarBien(request, item_id):
    instance = Bien.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('bienes')
    return render(request,'borrar_bien.html',{'instance': instance})


def crearInforme(request):
    error=None
    if request.method == 'POST':
        register_form = InformeForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('informes')
        else:
            error=register_form.errors
    else:
        register_form = InformeForm()
    return render(request,'nuevo_informe.html', {'form': register_form,'error': error})

def informes(request):
    items = InformeContable.objects.all().order_by('fecha')
    return render(request,'lista_informes.html', {'items': items })

def editarInforme(request, item_id):
    error=None
    instancia = InformeContable.objects.get(pk=item_id)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('informes')
        else:
            error=form.errors
    else:
        form = InformeForm(instance=instancia)

    return render(request,'editar_informe.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarInforme(request, item_id):
    instance = InformeContable.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('informes')
    return render(request,'borrar_informe.html',{'instance': instance})


def crearVehiculo(request):
    error=None
    if request.method == 'POST':
        register_form = VehiculoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('vehiculos')
        else:
            error=register_form.errors
    else:
        register_form = VehiculoForm()
    return render(request,'nuevo_vehiculo.html', {'form': register_form,'error': error})

def vehiculos(request):
    items = Vehiculo.objects.all().order_by('fecha')
    return render(request,'lista_vehiculos.html', {'items': items })

def editarVehiculo(request, item_id):
    error=None
    instancia = Vehiculo.objects.get(pk=item_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
        else:
            error=form.errors
    else:
        form = VehiculoForm(instance=instancia)

    return render(request,'editar_Vehiculo.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarVehiculo(request, item_id):
    instance = Vehiculo.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('vehiculos')
    return render(request,'borrar_Vehiculo.html',{'instance': instance})


def crearProducto(request):
    error=None
    if request.method == 'POST':
        register_form = ProductoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('productos')
        else:
            error=register_form.errors
    else:
        register_form = ProductoForm()
    return render(request,'nuevo_producto.html', {'form': register_form,'error': error})

def productos(request):
    items = Producto.objects.all()
    return render(request,'lista_productos.html', {'items': items })

def editarProducto(request, item_id):
    error=None
    instancia = Producto.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            error=form.errors
    else:
        form = ProductoForm(instance=instancia)

    return render(request,'editar_Producto.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarProducto(request, item_id):
    instance = Producto.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('productos')
    return render(request,'borrar_Producto.html',{'instance': instance})


def crearConsultaEmpleado(request):
    error=None
    if request.method == 'POST':
        register_form = ConsultaEmpleadoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('ConsultaEmpleado')
        else:
            error=register_form.errors
    else:
        register_form = ConsultaEmpleadoForm()
    return render(request,'nuevo_ConsultaEmpleado.html', {'form': register_form,'error': error})

def ConsultaEmpleados(request):
    items = ConsultaEmpleado.objects.all()
    return render(request,'lista_ConsultaEmpleado.html', {'items': items })

def editarConsultaEmpleado(request, item_id):
    error=None
    instancia = ConsultaEmpleado.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ConsultaEmpleadoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('ConsultaEmpleados')
        else:
            error=form.errors
    else:
        form = ConsultaEmpleadoForm(instance=instancia)

    return render(request,'editar_ConsultaEmpleado.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarConsultaEmpleado(request, item_id):
    instance = ConsultaEmpleado.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('ConsultaEmpleados')
    return render(request,'borrar_ConsultaEmpleado.html',{'instance': instance})

def crearCliente(request):
    error=None
    if request.method == 'POST':
        register_form = ClienteForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('Clientes')
        else:
            error=register_form.errors
    else:
        register_form = ClienteForm()
    return render(request,'nuevo_Cliente.html', {'form': register_form,'error': error})

def Clientes(request):
    items = Cliente.objects.all()
    return render(request,'lista_Clientes.html', {'items': items })

def editarCliente(request, item_id):
    error=None
    instancia = Cliente.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('Clientes')
        else:
            error=form.errors
    else:
        form = ClienteForm(instance=instancia)

    return render(request,'editar_Cliente.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarCliente(request, item_id):
    instance = Cliente.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('Clientes')
    return render(request,'borrar_Cliente.html',{'instance': instance})

def crearConsultaAlquiler(request):
    error=None
    if request.method == 'POST':
        register_form = ConsultaAlquilerForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('ConsultaAlquileres')
        else:
            error=register_form.errors
    else:
        register_form = ConsultaAlquilerForm()
    return render(request,'nuevo_ConsultaAlquiler.html', {'form': register_form,'error': error})

def ConsultaAlquileres(request):
    items = ConsultaAlquiler.objects.all().order_by('fecha')
    return render(request,'lista_ConsultaAlquiler.html', {'items': items })

def editarConsultaAlquiler(request, item_id):
    error=None
    instancia = ConsultaAlquiler.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ConsultaAlquilerForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('ConsultaAlquileres')
        else:
            error=form.errors
    else:
        form = ConsultaAlquilerForm(instance=instancia)

    return render(request,'editar_ConsultaAlquiler.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarConsultaAlquiler(request, item_id):
    instance = ConsultaAlquiler.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('ConsultaAlquileres')
    return render(request,'borrar_ConsultaAlquiler.html',{'instance': instance})

def crearSolicitaAlquiler(request):
    error=None
    if request.method == 'POST':
        register_form = SolicitaAlquilerForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('SolicitaAlquileres')
        else:
            error=register_form.errors
    else:
        register_form = SolicitaAlquilerForm()
    return render(request,'nuevo_SolicitaAlquiler.html', {'form': register_form,'error': error})

def SolicitaAlquileres(request):
    items = SolicitaAlquiler.objects.all()
    return render(request,'lista_SolicitaAlquiler.html', {'items': items })

def editarSolicitaAlquiler(request, item_id):
    error=None
    instancia = SolicitaAlquiler.objects.get(pk=item_id)
    if request.method == 'POST':
        form = SolicitaAlquilerForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('SolicitaAlquileres')
        else:
            error=form.errors
    else:
        form = SolicitaAlquilerForm(instance=instancia)

    return render(request,'editar_SolicitaAlquiler.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarSolicitaAlquiler(request, item_id):
    instance = SolicitaAlquiler.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('SolicitaAlquiler')
    return render(request,'borrar_SolicitaAlquiler.html',{'instance': instance})

def crearContiene(request):
    error=None
    if request.method == 'POST':
        register_form = ContieneForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('contiene')
        else:
            error=register_form.errors
    else:
        register_form = ContieneForm()
    return render(request,'nuevo_cambio.html', {'form': register_form,'error': error})

def contiene(request):
    items = Contiene.objects.all().order_by('fecha')
    return render(request,'lista_contiene.html', {'items': items })

def editarContiene(request, item_id):
    error=None
    instancia = Contiene.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ContieneForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('contiene')
        else:
            error=form.errors
    else:
        form = ContieneForm(instance=instancia)

    return render(request,'editar_contiene.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarContiene(request, item_id):
    instance = Contiene.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('contiene')
    return render(request,'borrar_contiene.html',{'instance': instance})
