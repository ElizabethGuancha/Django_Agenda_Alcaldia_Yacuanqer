from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Usuario)
#admin.site.register(Conductor)
#admin.site.register(TipoTransporte)
#admin.site.register(Mantenimiento)
#admin.site.register(Vehiculo)

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
      list_display = ('id_usuario', 'id_transporte', 'turno_agenda_inicio', 'turno_agenda_final', 'direccion','costo')
      ordering = ('id_usuario',)
      list_filter = ('id_usuario', 'turno_agenda_inicio', 'turno_agenda_final')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
      list_display = ('nombre','apellido', 'telefono', 'direccion')
      ordering = ('nombre',)
      search_fields = ('nombre', 'apellido')

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
      list_display = ('nombre','apellido', 'telefono')
      ordering = ('nombre',)
      search_fields = ('nombre', 'apellido')  

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
      list_display = ('tipo_transporte','cambio_aceite', 'cambio_llanta', 'observacion')
      ordering = ('tipo_transporte',)
      list_filter = ('tipo_transporte',)

 
@admin.register(TipoTransporte)
class TipoTransporteAdmin(admin.ModelAdmin):
      list_display = ('transporte','modelo')
      ordering = ('transporte',)
      list_filter = ('transporte',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
      list_display = ('id_transporte','institucion', 'placa', 'soat_exp', 'soat_ven', 'poliza_exp', 'poliza_ven', 'tecno_mecanico_exp', 'tecno_mecanico_ven')
      ordering = ('placa',)
      search_fields = ('institucion', 'placa')              
 
#admin.site.register(Agenda)


