from urllib.request import Request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from avatar.forms import  AvatarForm
from avatar.models import Avatar



# Create your views here.
def avatar_create(request):
    print('avatar')

    if request.method == "POST":
       form = AvatarForm(request.POST,request.FILES)
       print(form)
       if form.is_valid():
             form.save()           
             print("38")
             return redirect('core:usersadmin')   
    else:               
        form = AvatarForm()
        return render(request, "avatar/load_avatar.html",{"form": form})

  
    