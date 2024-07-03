from django.contrib import admin

# Register your models here.
from .models import *

class MonedaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sigla", "simbolo")

class AsientoAdmin(admin.ModelAdmin):
    list_display = ("fecha", "desc", "estado")
    list_filter = ("desc", "estado")

admin.site.register(Cuenta)
admin.site.register(Subcuenta)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Asiento, AsientoAdmin)
