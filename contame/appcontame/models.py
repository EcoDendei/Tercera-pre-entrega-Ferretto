from django.db import models

# Create your models here.

# Class Asiento contable
class Asiento(models.Model):
    
    ESTADOS_ASIENTOS = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    
    fecha = models.DateField()
    #usuario = models.CharField(max_length=50) #Aca deberia asociar al usuario que creo el asiento o podria asociar a quien corresponde el gasto, podriamos tener algo como centros de costos tambien
    estado = models.CharField(choices=ESTADOS_ASIENTOS, default='ACTIVO', max_length=8)
    desc = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.desc}"
    
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""
# Class Cuentas
class Cuenta(models.Model):
    
    nombre = models.CharField(max_length=50)    
    
    def __str__(self):
        return f"{self.nombre}"
    
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""
# Class Monedas
class Moneda(models.Model):
    
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)
    simbolo = models.CharField(max_length=1)
    
    def __str__(self):
        return f"{self.nombre}"
    
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""
# Class Subcuentas
class Subcuenta(models.Model):
    
    TIPOS_CUENTAS = (
        ('INGRESO', 'Ingresos'),
        ('EGRESO', 'Egresos'),
        ('OTRO', 'Otro'),
    )
    
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(choices=TIPOS_CUENTAS, default='OTRO', max_length=7)
    desc = models.CharField(max_length=250)
    moneda = models.ForeignKey('Moneda',on_delete=models.PROTECT)
    cuenta = models.ForeignKey('Cuenta',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre}"
    
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""

# Class Moviento, los movimientos que genero el asiento en las distintas cuentas
class Movimiento(models.Model):
    
    asiento = models.ForeignKey('Asiento',on_delete=models.CASCADE)
    monto = models.FloatField()
    cuenta = models.ForeignKey('Subcuenta',on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.asiento} - {self.monto}"
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""
