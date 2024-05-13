from django.urls import path

from producto.views import  index , productoNuevo_create

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("producto/create",productoNuevo_create, name="productoNuevo_create"),
    
]