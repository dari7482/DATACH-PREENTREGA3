from django.urls import path

from producto.views import  index , productoNuevo_create,producto_detail,producto_edit,producto_delete
app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("producto/create",productoNuevo_create, name="productoNuevo_create"),   
    path("producto/detail/<int:pk>",producto_detail, name="producto_detail"),
    path("producto/delete/<int:pk>",producto_delete, name="producto_delete"),
    path("producto/edit/<int:pk>",producto_edit, name="producto_edit"),
    
]