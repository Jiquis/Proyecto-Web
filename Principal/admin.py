from django.contrib import admin
from Principal import models
# Register your models here.

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre_usuario', 'nombres', 'apellido_paterno', 'apellido_materno', 'correo', 'saldo', 'edad', 'password')
    search_fields = ['id_usuario', 'nombre_usuario', 'correo']
    ordering = ['id_usuario']

@admin.register(models.Apuesta)
class ApuestaAdmin(admin.ModelAdmin):
    list_display = ('id_apuesta', 'nombre_apuesta', 'id_usuario', 'monto', 'fecha_apuesta')
    search_fields = ['id_apuesta', 'nombre_apuesta']

@admin.register(models.TipoApuesta)
class TipoApuestaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo', 'id_Apuesta', 'descripcion_tipo')
    search_fields = ['id_apuesta', 'id_tipo']

@admin.register(models.Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_evento', 'id_deporte', 'nombre_evento', 'fecha', 'EstadoEvento')
    search_fields = ['id_evento', 'id_deporte', 'nombre_evento', 'EstadoEvento']

@admin.register(models.ApuestaEvento)
class ApuestaEventoAdmin(admin.ModelAdmin):
    list_display = ('id_apuesta', 'id_evento', 'id_tipo', 'monto', 'EstadoEvento')
    search_fields = ['id_apuesta', 'id_evento', 'id_tipo', 'EstadoEvento']

@admin.register(models.Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('id_deporte', 'deporte')
    search_fields = ['id_deporte', 'deporte']

@admin.register(models.Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('id_participante', 'id_deporte', 'descripcion', 'nacionalidad', 'fecha_nacimiento', 'twitter', 'facebook')
    search_fields = ['id_participante', 'id_deporte', 'nacionalidad']

