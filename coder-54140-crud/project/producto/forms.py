from django import forms

from . import models


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "categoria","tipo_prod_id","editorial_id"]