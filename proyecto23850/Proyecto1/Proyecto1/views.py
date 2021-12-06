from django.http import HttpResponse
from datetime import datetime 
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django, en Coder.")

def segundaVista(request):
    return HttpResponse("<br><br> Soy admin.")

def dia(request):
    
    variable = datetime.now() 
    
    return HttpResponse(f'Fecha y Hora:<br><br> {variable} ')

def apellido(request, ape):

    fecha = datetime.now()
    return HttpResponse(f'El profe de Python {ape} es crack. <br><br> Ah, y hoy es {fecha}')

def probandoTemplate(request):
     

    mejorEstudiante = "Alberto Nisman"

    nota = 8.9

    fecha = datetime.now()

    estudiantesPiolas = ["Juan", "Pedro", "Lucas"]
    
    dicc = {"nombre":mejorEstudiante,"nota":nota,"fecha":fecha, "estudiantes":estudiantesPiolas}
    
    template = loader.get_template("template1.html")
    
    #miHTML = open("C:/Users/Osuna/Desktop/proyecto23850/Proyecto1/Proyecto1/templates/template1.html")
    
    #plantilla = Template(miHTML.read())

    #miHTML.close() 

    #miContexto = Context(dicc) #datos que envío a mi web.

    #documento = plantilla.render(miContexto)

    documento = template.render(dicc)

    return HttpResponse(documento)