from django.db import models
import json
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=25, unique=True, default='')
    apellido_paterno = models.CharField(max_length=25, default='')  
    apellido_materno = models.CharField(max_length=25, default='')  
    nombres = models.CharField(max_length=50, default='') 
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default='')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    edad = models.IntegerField()

    def __str__(self):  
        return f"{self.id_usuario} - {self.nombre_usuario}"  


'''
class UsuarioVIP(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    beneficios_vip = models.JSONField(default=dict)

    def str(self):
        return f"VIP - {self.usuario.nombre}"
'''
class Apuesta(models.Model):
    id_apuesta = models.AutoField(primary_key=True)
    nombre_apuesta = models.CharField(max_length=100, default='')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def str(self):
        return f"{self.id_apuesta} - Usuario: {self.id_usuario.nombre_usuario}, Monto: {self.monto}"
    
class TipoApuesta(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    id_Apuesta = models.ForeignKey(Apuesta, on_delete=models.CASCADE)
    descripcion_tipo = models.CharField(max_length=100)

    def str(self):
        return f"{self.id_tipo} - Apuesta: {self.id_Apuesta.nombre_apuesta}, Descripcion: {self.descripcion_tipo}"


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    id_deporte = models.ForeignKey('Deporte', on_delete=models.CASCADE)  # 'Deporte' se coloca entre comillas para evitar problemas de importación circular
    nombre_evento = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ESTADO_EVENTO_CHOICES = [
        ('FUTURO', 'Futuro'),
        ('ACTIVO', 'Activo'),
        ('TERMINADO', 'Terminado'),
    ]
    EstadoEvento = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='FUTURO')

    def str(self):
        return f"{self.NombreEvento} ({self.idDeporte.NombreDeporte}), Fecha: {self.fecha}, Estado: {self.EstadoEvento}"

class ApuestaEvento(models.Model):
    id_apuesta = models.OneToOneField(Apuesta, on_delete=models.CASCADE, primary_key=True)
    id_tipo = models.ForeignKey(TipoApuesta, on_delete=models.CASCADE)
    id_evento = models.ForeignKey('Evento', on_delete=models.CASCADE)  # 'Evento' se coloca entre comillas para evitar problemas de importación circular
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    ESTADO_EVENTO_CHOICES = [
        ('FUTURO', 'Futuro'),
        ('ACTIVO', 'Activo'),
        ('TERMINADO', 'Terminado'),
    ]
    EstadoEvento = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='FUTURO')

    def str(self):
        return f"Apuesta: {self.id_apuesta.nombre_apuesta}, Tipo: {self.id_tipo.descripcion_tipo}, Evento: {self.id_evento.nombre_evento}, Monto: {self.monto}, Estado: {self.EstadoEvento}"
    




class Deporte(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    deporte = models.CharField(max_length=50)

    def str(self):
        return self.deporte
    
class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombre_participante = models.CharField(max_length=100)
    id_deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def str(self):
        return f"{self.NombreParticipante} ({self.id_deporte.deporte})"