from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('asientos/', asientos, name="asientos"),
    path('cuentas/', cuentas, name="cuentas"),
    path('subcuentas/', subcuentas, name="subcuentas"),
    path('movimientos/', movimientos, name="movimientos"),
    path('monedas/', monedas, name="monedas"),
    path('acerca/', acerca, name="acerca"),
    path('monedas/moneda_form/', monedaForm, name="monedaForm"),
    path('cuentas/cuenta_form/', cuentaForm, name="cuentaForm"),
    path('subcuentas/subcuenta_form/', subcuentaForm, name="subcuentaForm"),
    path('asientos/asiento_form/', asientoForm, name="asientoForm"),
    path('cuentas/buscar_cuentas/', buscarCuentas, name="buscarCuentas"),
    path('cuentas/encontrar_cuentas/', encontrarCuentas, name="encontrarCuentas"),
]

