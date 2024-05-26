from django.urls import path


from avatar.views import  avatar_create
app_name = "avatar"

urlpatterns = [  
    path("avatar/create",avatar_create, name="avatar_create"),   
    
]


