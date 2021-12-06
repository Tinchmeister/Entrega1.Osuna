from django.urls import path 
from AppCoder import views

urlpatterns = [

   path('inicio/', views.inicio),
   path('inicio/jugadores/', views.jugadores),
     
     

 ]
