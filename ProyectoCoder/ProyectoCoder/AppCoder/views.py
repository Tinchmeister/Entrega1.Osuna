from django.forms.formsets import MIN_NUM_FORM_COUNT
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import BandaFormulario, MusicoFormulario, ContactoFormulario
from AppCoder.models import Banda, Musico, Contacto



# Create your views here.




def inicio(request):

    #return HttpResponse("Prueba de inicio")
    return render(request, 'AppCoder/inicio.html')






def produccion(request):

   
    return render(request, 'AppCoder/produccion.html')


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
