from django.http import HttpResponse
from datetime import datetime 
from django.template import Template, Context

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
     #LAS BARRAS TIENEN QUE SER " / " 
    
    miHTML = open("C:/Users/Osuna/Desktop/proyecto23850/Proyecto1/Proyecto1/templates/template1.html")
    
    plantilla = Template(miHTML.read())

    miHTML.close() 

    miContexto = Context() #datos que envío a mi web.

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)