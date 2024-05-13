from django.contrib import admin

# Register your models here.


from .models import Producto,Editorial,Categoria

admin.site.register(Producto)
admin.site.register(Editorial)
admin.site.register(Categoria)