from django.forms.formsets import MIN_NUM_FORM_COUNT
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

#CRUD DJANGO

#READ/LEER:
class BandaList(ListView):

    model = Banda
    template_name = "AppCoder/banda_list.html"

#Ver más (PIJA AHRe)

class BandaDetalle(DetailView):

    model = Banda
    template_name = "AppCoder/banda_detalle.html"

#Crear

class BandaCreacion(CreateView):

    model = Banda
    success_url = "../AppCoder/banda/list"
    fields = ["nombre", "generoMusical", "instrumentoBuscado"]

#Modificar

class BandaUpdate(UpdateView):

    model = Banda
    success_url = "../banda/list"
    fields = ["nombre", "generoMusical", "instrumentoBuscado"]

#DELET DIS

class BandaDelete(DeleteView):

    model = Banda
    success_url = "../banda/list"



class MusicoList(ListView):

    model = Musico
    template_name = "AppCoder/musico_list.html"



class MusicoDetalle(DetailView):

    model = Musico
    template_name = "AppCoder/musico_detalle.html"



class MusicoCreacion(CreateView):

    model = Musico
    success_url = "../AppCoder/musico/list"
    fields = ["nombre", "apellido", "fechaNacimiento", "instrumento", "esNovato"]



class MusicoUpdate(UpdateView):

    model = Musico
    success_url = "../musico/list"
    fields = ["nombre", "apellido", "fechaNacimiento", "instrumento", "esNovato"]



class MusicoDelete(DeleteView):

    model = Musico
    success_url = "../musico/list"






def inicio(request):

    #return HttpResponse("Prueba de inicio")
    return render(request, 'AppCoder/inicio.html')






def produccion(request):

   
    return render(request, 'AppCoder/produccion.html')

@login_required
def bandaFormulario(request):

    if request.method == "POST":
        
        miFormulario = BandaFormulario(request.POST)
        
        if miFormulario.is_valid():
                
            informacion = miFormulario.cleaned_data
            bandaInstancia = Banda(

            nombre = informacion["nombre"],
            generoMusical = informacion["generoMusical"],
            instrumentoBuscado = informacion["instrumentoBuscado"]

            )

            bandaInstancia.save()

            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = BandaFormulario()

    

        
    return render(request,'AppCoder/bandaFormulario.html',{"miFormulario":miFormulario})

@login_required
def musicoFormulario(request):

    if request.method == "POST":
        
        miFormulario = MusicoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            musicoInstancia = Musico(

                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                fechaNacimiento = informacion["fechaNacimiento"],
                instrumento = informacion["instrumento"],
                esNovato = informacion["esNovato"],
                
            
            
            
            

            )                

                

            musicoInstancia.save()

            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = MusicoFormulario()

    

    return render(request,'AppCoder/musicoFormulario.html',{"miFormulario":miFormulario})

@login_required
def contactoFormulario(request):

    if request.method == "POST":
        
        miFormulario = ContactoFormulario(request.POST)
        
        if miFormulario.is_valid():
                
            informacion = miFormulario.cleaned_data
            contInstancia = Contacto(

                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                numero = informacion["numero"],
                mail = informacion["mail"],

            )

            contInstancia.save()

            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = ContactoFormulario()

    

        
    return render(request,'AppCoder/contactoFormulario.html',{"miFormulario":miFormulario})


def login_request(request):

    if request.method=="POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"{usuario}"})
            
            else:

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Error, ingrese nuevamente."})

        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Error de formulario."})



    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form":form} )

#Registro

def register(request):

    if request.method=="POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            form.save()

            return render(request, "AppCoder/inicio.html", {"mensaje": f"{username} Creado"})

    else:

        form = UserRegisterForm()

    return render(request, "AppCoder/register.html", {"form":form})

#Editar Perfil

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def bandasBusqueda(request):
    return render(request, 'AppCoder/bandasBusqueda.html')


def bandasBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        banda = Banda.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppCoder/bandasBusquedaResultado.html', {"banda":banda, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de una banda"
    return HttpResponse(output)



