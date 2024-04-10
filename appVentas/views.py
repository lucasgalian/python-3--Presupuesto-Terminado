from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Presupuesto, Cliente

from .forms import PresupuestoForm, ClienteForm

def home(request):
    return render(request, 'home.html')
########MOSTAR######
def listaPres(request):
    servicios= Presupuesto.objects.all()
    return render(request, 'listaPres.html',{'servicios': servicios})   

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes.html',
                  {'clientes':clientes})


def detalle(request, id):
    if  Cliente.id:
        cliente= get_object_or_404(Cliente,id=id)
        return render(request, 'detalle.html',{'cliente':cliente})
    else :
        Presupuesto.id ==True
        presupuesto= get_object_or_404(Presupuesto, id=id)
        return render(request,'detalle.html', {'presupuesto':presupuesto})


        

#####FORMULARIO CREATE#####


def create_pres(request):
    if request.method=='POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaPres')
    else:
        form = PresupuestoForm()
    return render(request, 'create_pres.html',{'form':form})                  


def create_cli(request):
    if request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form =  ClienteForm()
    return render(request, 'create_cli.html',{'form':form})                  
####MODIFICAR###
def updatePres(request,id):
    presupuesto= get_object_or_404(Presupuesto, id= id)
    if request.method == "POST":
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():                                                            
            form.save()
            return redirect('listaPres')
        else:
           print("error")
    else:
        form= PresupuestoForm(instance=presupuesto)        
        return render(request,
              'create_pres.html', {'form':form})
def updateCli(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redirige a donde desees después de modificar el presupuesto
        else:
            print('error')        
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'create_cli.html', {'form': form})

def deletePres(request, id):
        presupuesto = get_object_or_404(Presupuesto, id=id)
        if request.method == 'POST':
            presupuesto.delete()
            return redirect('listaPres') # Redirige a donde desees después de borrar el presupuesto
        return render(request, 'delete.html', {'presupuesto': presupuesto})

def deleteCli(request, id):
        cliente = get_object_or_404(Cliente, id=id)
        if request.method=='POST':
            cliente.delete()
            return redirect('clientes')
        return render(request, 'delete.html',{'cliente':cliente})