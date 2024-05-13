
from django.shortcuts import render , redirect

from producto.forms import ProductoCategoriaForm
from producto.models import Producto



# Create your views here.
def index(request):
     consulta = Producto.objects.all()
     print(consulta)
     contexto = {"productocategoria": consulta} 
     print(contexto)
      
     return render(request, "producto/index.html",contexto)

def productoNuevo_create(request):
     print(18)
     if request.method == "POST":
        print("post")
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")    
     else:
          form = ProductoCategoriaForm()
          return render(request, "producto/productocategoria_create.html", {"form": form})


    