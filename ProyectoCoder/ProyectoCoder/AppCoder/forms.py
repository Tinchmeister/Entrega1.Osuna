from django import forms 
import datetime


class BandaFormulario(forms.Form):
    
    #campos visibles en la web

    nombre = forms.CharField(max_length=40)  
    generoMusical= forms.CharField(max_length=40)
    instrumentoBuscado = forms.CharField(max_length=40)

    


class MusicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    fechaNacimiento = forms.DateField(initial=datetime.date.today)
    instrumento = forms.CharField(max_length=40)
    esNovato = forms.BooleanField()

class ContactoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    mail = forms.CharField(max_length=40)


    

