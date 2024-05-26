from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from .forms import CustomAuthenticationForm, CustomUserCreationForm
# Create your views here.

def index(request):
    return render(request, "core/index.html")


class CustomLoginView(LoginView):
     authentication_form = CustomAuthenticationForm    
     template_name="core/login.html"
     

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/index.html", {"mensaje": f"Usuario '{username}' creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})


def usersadmin(request):
    users = User.objects.all() 
    print(users[0].__dict__)  
    return render(request, "core/listado_user.html", {"users": users})