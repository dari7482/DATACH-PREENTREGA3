from django import forms

from . import models


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "categoria","tipo_prod_id","editorial_id","precio"]


class ProductoDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "tipo_prod_id"]



