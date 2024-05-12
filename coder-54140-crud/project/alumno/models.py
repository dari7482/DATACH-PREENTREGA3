
from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"



class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="país de origen"
    )
    documento= models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Alumnos"
        verbose_name_plural = "Alumnos"

