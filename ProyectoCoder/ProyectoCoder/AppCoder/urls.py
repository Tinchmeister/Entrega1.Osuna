from django.urls import path 
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

   path('inicio/', views.inicio, name="Inicio"),
   path('bandaFormulario', views.bandaFormulario, name="Banda"),
   path('musicoFormulario', views.musicoFormulario, name="Musico"),  
   path('produccion', views.produccion, name="Produccion"),  
   path('contactoFormulario', views.contactoFormulario, name="Contacto"),

  #Login/Registro
    path('login', views.login_request, name="Login"),
    path('inicioLogin', views.inicioLogin, name="InicioLogin"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),


  
     

 ]
