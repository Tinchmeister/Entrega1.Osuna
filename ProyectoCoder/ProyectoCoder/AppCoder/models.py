from django.db import models
import datetime

# Create your models here.




class Banda(models.Model):
    nombre = models.CharField(max_length=40)  
    generoMusical= models.CharField(max_length=40)
    instrumentoBuscado = models.CharField(max_length=40)

    def __str__(self):
        return f"NOMBRE: {self.nombre} - GENERO: {self.generoMusical} - INSTRUMENTO BUSCADO: {self.instrumentoBuscado}"

class Musico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaNacimiento = models.DateField(default=datetime.date.today)
    instrumento = models.CharField(max_length=40)
    esNovato = models.BooleanField()

    def __str__(self):
        return f"NOMBRE: {self.nombre} - APELLIDO: {self.apellido} - INSTRUMENTO: {self.instrumento}"


'''class Productor(models.Model):
    nombreApellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=40)'''

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    mail = models.CharField(max_length=40)

