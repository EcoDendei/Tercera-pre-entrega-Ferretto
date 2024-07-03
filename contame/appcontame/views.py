from django.shortcuts import render
from .models import *
from .forms import *

# Pagina principal view
def home(request):
    return render(request, "appcontame/index.html")

def asientos(request):
    contexto = {"asientos": Asiento.objects.all()}
    return render(request, "appcontame/asientos.html", contexto)

def cuentas(request):
    contexto = {"cuentas": Cuenta.objects.all()}
    return render(request, "appcontame/cuentas.html", contexto)

def subcuentas(request):
    contexto = {"subcuentas": Subcuenta.objects.all(), "monedas": Moneda.objects.all()}
    return render(request, "appcontame/subcuentas.html", contexto)

def movimientos(request):
    contexto = {"movimientos": Movimiento.objects.all()}
    return render(request, "appcontame/movimientos.html", contexto)

def monedas(request):
    contexto = {"monedas": Moneda.objects.all()}
    return render(request, "appcontame/monedas.html", contexto)

def acerca(request):
    return render(request, "appcontame/acerca.html")

# Seccion de formularios
def monedaForm(request):
    if request.method == 'POST':
        miForm = MonedaForm(request.POST)
        if miForm.is_valid():
            moneda_nombre = miForm.cleaned_data.get("nombre")
            moneda_sigla = miForm.cleaned_data.get("sigla")
            moneda_simbolo = miForm.cleaned_data.get("simbolo")
            moneda = Moneda(nombre=moneda_nombre, sigla=moneda_sigla, simbolo=moneda_simbolo)
            moneda.save()
            contexto = {"monedas": Moneda.objects.all() }
            return render(request, "appcontame/monedas.html", contexto)
    else:
        miMonedaForm = MonedaForm()
        
    return render(request, "appcontame/monedaForm.html", {"form": miMonedaForm})

def cuentaForm(request):
    if request.method == 'POST':
        miForm = CuentaForm(request.POST)
        if miForm.is_valid():
            cuenta_nombre = miForm.cleaned_data.get("nombre")
            cuenta = Cuenta(nombre=cuenta_nombre)
            cuenta.save()
            contexto = {"cuentas": Cuenta.objects.all() }
            return render(request, "appcontame/cuentas.html", contexto)
    else:
        miCuentaForm = CuentaForm()
        
    return render(request, "appcontame/cuentaForm.html", {"form": miCuentaForm})

def subcuentaForm(request):
    if request.method == 'POST':
        miForm = SubcuentaForm(request.POST)
        if miForm.is_valid():
            subcuenta_nombre = miForm.cleaned_data.get("nombre")
            subcuenta_activo = miForm.cleaned_data.get("activo")
            subcuenta_tipo = miForm.cleaned_data.get("tipo")
            subcuenta_desc = miForm.cleaned_data.get("desc")
            subcuenta_moneda = miForm.cleaned_data.get("moneda")
            moneda = Moneda.objects.all().filter(id=subcuenta_moneda)
            subcuenta_cuenta = miForm.cleaned_data.get("cuenta")
            subcuenta = Subcuenta(nombre=subcuenta_nombre, activo=subcuenta_activo, tipo=subcuenta_tipo, desc=subcuenta_desc, moneda=moneda, cuenta=subcuenta_cuenta)
            subcuenta.save()
            contexto = {"subcuentas": Subcuenta.objects.all() }
            return render(request, "appcontame/subcuentas.html", contexto)
    else:
        miSubcuentaForm = SubcuentaForm()
        
    return render(request, "appcontame/subcuentaForm.html", {"form": miSubcuentaForm})

def asientoForm(request):
    if request.method == 'POST':
        miForm = AsientoForm(request.POST)
        if miForm.is_valid():
            asiento_fecha = miForm.cleaned_data.get("fecha")
            asiento_desc = miForm.cleaned_data.get("desc")
            asiento_estado = miForm.cleaned_data.get("estado")
            
            asiento = Asiento(fecha=asiento_fecha, desc=asiento_desc, estado=asiento_estado)
            asiento.save()
            contexto = {"asientos": Asiento.objects.all() }
            return render(request, "appcontame/asientos.html", contexto)
    else:
        miAsientoForm = AsientoForm()
        
    return render(request, "appcontame/asientoForm.html", {"form": miAsientoForm})

# Seccion de busquedas
def buscarCuentas(request):
    return render(request, "appcontame/buscar.html")

def encontrarCuentas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=patron) 
    else:
        cuentas = Cuenta.objects.all()
        
    contexto = {'cuentas': cuentas}
    return render(request, "appcontame/cuentas.html", contexto)