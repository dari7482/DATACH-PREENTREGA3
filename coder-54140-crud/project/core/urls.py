from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views

from core.views import CustomLoginView, index, register,usersadmin

app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("adminuser/", usersadmin, name="usersadmin"),
    
]
urlpatterns += staticfiles_urlpatterns()

#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)