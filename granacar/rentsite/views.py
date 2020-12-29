# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .filters import *

def index(request):
    return render(request,'base.html')

def crearPuesto(request):
    error=None
    if request.method == 'POST':
        register_form = PuestoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('Puestos')
        else:
            error=register_form.errors
    else:
        register_form = PuestoForm()
    return render(request,'nuevo_puesto.html', {'form': register_form,'error': error})

def Puestos(request):
    items = Puesto.objects.all()

    myFilter = PuestoFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_puestos.html', {'items': items, 'myFilter':myFilter})

def editarPuesto(request, item_id):
    error=None
    instancia = Puesto.objects.get(pk=item_id)
    if request.method == 'POST':
        form = PuestoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('Puestos')
        else:
            error=form.errors
    else:
        form = PuestoForm(instance=instancia)
    
    return render(request,'editar_puesto.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarPuesto(request, item_id):
    instance = Puesto.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('Puestos')
    return render(request,'borrar_Puesto.html',{'instance': instance})


def crearEmpleado(request):
    error=None
    if request.method == 'POST':
        register_form = EmpleadoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('empleados')
        else:
            error=register_form.errors
    else:
        register_form = EmpleadoForm()
    return render(request,'nuevo_empleado.html', {'form': register_form,'error': error})


def empleados(request):
    items = EmpleadoTrabaja.objects.all() 
    myFilter = EmpleadoTrabajaFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_empleados.html', {'items': items, 'myFilter':myFilter}) # Aquí van la las variables para la plantilla


def editarEmpleado(request, item_id):
    instancia = EmpleadoTrabaja.objects.get(pk=item_id)

    form = EmpleadoForm(instance=instancia)
    error=None
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect(empleados)
        else:
            error=form.errors

    return render(request,'editar_empleado.html', {'register_form': form, 'item_id':item_id, 'error':error})

def borrarEmpleado(request, item_id):
    instance = EmpleadoTrabaja.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('empleados')
    return render(request,'borrar_Empleado.html',{'instance': instance})



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
    myFilter = FacturaFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_facturas.html', {'items': items, 'myFilter':myFilter})


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
    myFilter = BienFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_bienes.html', {'items': items, 'myFilter':myFilter})


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
    myFilter = InformeFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_informes.html', {'items': items, 'myFilter':myFilter})


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
    items = Vehiculo.objects.all()
    myFilter = VehiculoFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_vehiculos.html', {'items': items, 'myFilter':myFilter})


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

    return render(request,'editar_vehiculo.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarVehiculo(request, item_id):
    instance = Vehiculo.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('vehiculos')
    return render(request,'borrar_vehiculo.html',{'instance': instance})


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
    myFilter = ProductoFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_productos.html', {'items': items, 'myFilter':myFilter})


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

    return render(request,'editar_producto.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarProducto(request, item_id):
    instance = Producto.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('productos')
    return render(request,'borrar_producto.html',{'instance': instance})


def crearConsultaEmpleado(request):
    error=None
    if request.method == 'POST':
        register_form = ConsultaEmpleadoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('ConsultaEmpleados')
        else:
            error=register_form.errors
    else:
        register_form = ConsultaEmpleadoForm()
    return render(request,'nuevo_ConsultaEmpleado.html', {'form': register_form,'error': error})

def ConsultaEmpleados(request):
    items = ConsultaEmpleado.objects.all()
    myFilter = ConsultaEmpleadoFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_ConsultaEmpleado.html', {'items': items, 'myFilter':myFilter})

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
    myFilter = ClienteFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_Clientes.html', {'items': items, 'myFilter':myFilter})

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
    items = ConsultaAlquiler.objects.all()
    myFilter = ConsultaAlquilerFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_ConsultaAlquiler.html', {'items': items, 'myFilter':myFilter})

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
    myFilter = SolicitaAlquilerFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_SolicitaAlquiler.html', {'items': items, 'myFilter':myFilter})


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
        return redirect('SolicitaAlquileres')
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
    return render(request,'nuevo_contiene.html', {'form': register_form,'error': error})

def contiene(request):
    items = Contiene.objects.all()
    myFilter = ContieneFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_contiene.html', {'items': items, 'myFilter':myFilter})

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

def crearBalanceFinanciero(request):
    error=None
    if request.method == 'POST':
        register_form = BalanceFinancieroForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('balanaceFinancieros')
        else:
            error=register_form.errors
    else:
        register_form = BalanceFinancieroForm()
    return render(request,'nuevo_balanaceFinanciero.html', {'form': register_form,'error': error})

def balanaceFinancieros(request):
    items = BalanceFinanciero.objects.all().order_by('fecha_realizacion')
    myFilter = BalanceFinancieroFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_balanaceFinancieros.html', {'items': items, 'myFilter':myFilter})

def editarBalanceFinanciero(request, item_id):
    error=None
    instancia = BalanceFinanciero.objects.get(pk=item_id)
    if request.method == 'POST':
        form = BalanceFinancieroForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('balanaceFinancieros')
        else:
            error=form.errors
    else:
        form = BalanceFinancieroForm(instance=instancia)
    
    return render(request,'editar_BalanceFinanciero.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarBalanceFinanciero(request, item_id):
    instance = BalanceFinanciero.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('balanaceFinancieros')
    return render(request,'borrar_BalanceFinanciero.html',{'instance': instance})

def crearConsultaInformeContable(request):
    error=None
    if request.method == 'POST':
        register_form = ConsultaInformeContableForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('ConsultaInformeContables')
        else:
            error=register_form.errors
    else:
        register_form = ConsultaInformeContableForm()
    return render(request,'nuevo_ConsultaInformeContable.html', {'form': register_form,'error': error})

def ConsultaInformeContables(request):
    items = ConsultaInformeContable.objects.all()
    myFilter = ConsultaInformeContableFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_ConsultaInformeContables.html', {'items': items, 'myFilter':myFilter})

def editarConsultaInformeContable(request, item_id):
    error=None
    instancia = ConsultaInformeContable.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ConsultaInformeContableForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('ConsultaInformeContables')
        else:
            error=form.errors
    else:
        form = ConsultaInformeContableForm(instance=instancia)
    
    return render(request,'editar_ConsultaInformeContable.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarConsultaInformeContable(request, item_id):
    instance = ConsultaInformeContable.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('ConsultaInformeContables')
    return render(request,'borrar_ConsultaInformeContable.html',{'instance': instance})

def crearConsultaFactura(request):
    error=None
    if request.method == 'POST':
        register_form = ConsultaFacturaForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('ConsultaFacturas')
        else:
            error=register_form.errors
    else:
        register_form = ConsultaFacturaForm()
    return render(request,'nuevo_ConsultaFactura.html', {'form': register_form,'error': error})

def ConsultaFacturas(request):
    items = ConsultaFactura.objects.all()
    myFilter = ConsultaFacturaFilter(request.GET,queryset=items)
    items = myFilter.qs 

    return render(request,'lista_ConsultaFacturas.html', {'items': items, 'myFilter':myFilter})


def editarConsultaFactura(request, item_id):
    error=None
    instancia = ConsultaFactura.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ConsultaFacturaForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('ConsultaFacturas')
        else:
            error=form.errors
    else:
        form = ConsultaFacturaForm(instance=instancia)
    
    return render(request,'editar_ConsultaFactura.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarConsultaFactura(request, item_id):
    instance = ConsultaFactura.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('ConsultaFacturas')
    return render(request,'borrar_ConsultaFactura.html',{'instance': instance})


    




    


    

