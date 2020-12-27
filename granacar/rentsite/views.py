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


    



    


    
