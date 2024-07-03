from django import forms

class MonedaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    sigla = forms.CharField(max_length=3, required=True)
    simbolo = forms.CharField(max_length=1, required=True)
    
class CuentaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    
class SubcuentaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    activo = forms.BooleanField(required=True)
    tipo = forms.CharField(max_length=7, required=True)
    desc = forms.CharField(max_length=250)
    moneda = forms.IntegerField(required=True)
    cuenta = forms.IntegerField(required=True)

class AsientoForm(forms.Form):
    fecha = forms.DateField(required=True)
    desc = forms.CharField(max_length=200, required=True)
    estado = forms.CharField(max_length=8, required=True)