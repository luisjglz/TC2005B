from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    grupo = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre}, Gpo: {self.grupo}, Activo: {self.activo}'