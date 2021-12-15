from django.urls import path 
from AppCoder import views

urlpatterns = [

   path('inicio/', views.inicio, name="Inicio"),
   path('bandaFormulario', views.bandaFormulario, name="Banda"),
   path('musicoFormulario', views.musicoFormulario, name="Musico"),  
   path('produccion', views.produccion, name="Produccion"),  
   path('contactoFormulario', views.contactoFormulario, name="Contacto"),

  
     

 ]
