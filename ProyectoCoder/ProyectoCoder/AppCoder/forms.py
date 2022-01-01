from django import forms 
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class UserRegisterForm(UserCreationForm):
    
    #Necesarios
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    #Opcionales
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    #image_avatar = forms.ImageField(label='Imagen o Avatar', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']

  








   




    

