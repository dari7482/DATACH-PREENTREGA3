from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nombre


class Editorial(models.Model):

    nombre=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nombre






class Producto(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name="descripción",
        
    ),    
    categoria=models.CharField(max_length=20)
    tipo_prod_id=models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.SET_NULL,null=True)
    editorial_id=models.ForeignKey(Editorial, verbose_name="Editorial", on_delete=models.SET_NULL,null=True)
    precio= models.DecimalField(verbose_name="precio", max_digits=10, decimal_places=2,null=True)

    def __str__(self) -> str:
        """Retorna una instancia del modelo en forma de cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"


