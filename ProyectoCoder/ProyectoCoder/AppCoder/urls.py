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
 
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

   #CBV
   path('banda/list', views.BandaList.as_view(), name="List"),
   path(r'^(?P<pk>\d+)$', views.BandaDetalle.as_view(), name="Detail"),


   path(r'^nuevo$', views.BandaCreacion.as_view(), name='New'),
   path(r'^editar/(?P<pk>\d+)$', views.BandaUpdate.as_view(), name='Edit'),
   path(r'^borrar/(?P<pk>\d+)$', views.BandaDelete.as_view(), name='Delete'),
   
   path('musico/list', views.MusicoList.as_view(), name="MusicoList"),
   path(r'^musicoDetalle(?P<pk>\d+)$', views.MusicoDetalle.as_view(), name="MusicoDetail"),
   path(r'^musicoNuevo$', views.MusicoCreacion.as_view(), name='MusicoNew'),
   path(r'^musicoEditar/(?P<pk>\d+)$', views.MusicoUpdate.as_view(), name='MusicoEdit'),
   path(r'^musicoBorrar/(?P<pk>\d+)$', views.MusicoDelete.as_view(), name='MusicoDelete'),

    path('bandasBusqueda', views.bandasBusqueda, name="BandasBusqueda"),
    path('bandasBusquedaResultado/', views.bandasBusquedaResultado, name="BandasBusquedaResultado"),


    

  
    



  
     

 ]
