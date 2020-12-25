# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, redirect
from .forms import *

# Create your views here.

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



    
