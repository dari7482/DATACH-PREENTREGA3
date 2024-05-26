
from django.shortcuts import render , redirect

from producto.forms import ProductoCategoriaForm, ProductoDeleteForm
from producto.models import Producto



# Create your views here.
def index(request):
     busqueda= request.GET.get("busqueda",None)
     if busqueda:
          print(busqueda)        
          consulta = Producto.objects.filter(nombre__icontains=busqueda)
     else: 
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
          return render(request, "producto/productocategoria_form.html", {"form": form})





def producto_detail(request,pk:int):
     print(pk)
     query = Producto.objects.get(id=pk)
     print(query)
     contexto={"producto":query}
     return render(request,"producto/productocategoria_detail.html",contexto)

def producto_edit(request,pk:int):
     query = Producto.objects.get(id=pk)
     print(query)
     contexto={"producto":query}
     print(18)
     if request.method == "POST":
        print("post")
        form = ProductoCategoriaForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:index")    
     else:
          form = ProductoCategoriaForm(instance=query)
          return render(request, "producto/productocategoria_form.html", {"form": form})

    
def producto_delete(request,pk:int):
     query = Producto.objects.get(id=pk)
     print('72',query)
     if request.method=="POST":
          query.delete()
          return redirect("producto:index")    
     return render(request,"producto/productocategoria_confirm_delete.html",{"object":query})
          
     

