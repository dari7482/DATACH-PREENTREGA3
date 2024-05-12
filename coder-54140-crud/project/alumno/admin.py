from django.contrib import admin
from .models import Alumno, Pais
# Register your models here.
admin.site.register(Pais)
admin.site.register(Alumno)