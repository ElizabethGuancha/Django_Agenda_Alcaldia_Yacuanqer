from django.db import models

# Create your models here.
# Modelo Usuario
class Usuario(models.Model):
    ID_TYPE = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tareta de Identidad'),
        ('CE', 'Cedula de Extranjeria'),
        ('RC', 'Registro Civil')
    )

    GENDER_TYPE = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    nombre=models.CharField("Nombres", max_length=100)
    apellido=models.CharField("Apellidos", max_length=100)
    tipo=models.CharField("Tipo de Identificacion", max_length=5, choices=ID_TYPE)
    cedula=models.CharField("Cedula", max_length=10)
    genero=models.CharField("Genero", max_length=5, choices= GENDER_TYPE)
    telefono=models.CharField("Telefono", max_length=10)
    direccion=models.CharField("Dirección", max_length=200)

    class Meta:
        verbose_name = "Registrar Datos Del Usuario"
        verbose_name_plural ="Registrar Datos De los Usuarios"
    def __str__(self):
        return '{0} - {1}'.format(self.nombre,self.apellido)

# Modelo Conductor
class Conductor (models.Model):
   
    nombre=models.CharField("Nombres", max_length=100)
    apellido=models.CharField("Apellidos", max_length=100)
    telefono=models.CharField("Telefono", max_length=10)
       
    class Meta:
        verbose_name = "Registrar Datos Del Conductor"
        verbose_name_plural ="Registrar Datos De los Conductores"
    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)   

# Modelo Tipo transporte
class TipoTransporte (models.Model):
   
    transporte=models.CharField("Tipo Transporte", max_length=100)
    modelo=models.CharField("Modelo", max_length=100)
       
    class Meta:
        verbose_name = "Registrar Datos Del Transporte"
        verbose_name_plural ="Registrar Datos De los Transportes"
    def __str__(self):
        return '{0} - {1}'.format(self.transporte, self.modelo) 

# Modelo Mantenimiento
class Mantenimiento (models.Model):
    tipo_transporte=models.OneToOneField(TipoTransporte, on_delete=models.CASCADE, null=True, verbose_name="Lista De Vehiculos")
    cambio_aceite=models.DateField("Fecha Cambio De Aceite")
    cambio_llanta=models.DateField("Fecha Cambio De Llantas")
    observacion=models.CharField("Observaciones", max_length=1000)
    
    class Meta:
        verbose_name = "Registrar Datos Del Mantenimiento Del Vehiculo"
        verbose_name_plural ="Registrar Datos De los Mantenimientos De Los Vehiculos"
    def __str__(self):
        return 'Lista De Vehiculos: {0}'.format(self.tipo_transporte)  

# Modelo Vehiculo
class Vehiculo (models.Model):
  
    INSTITUCION_TYPE = (
        ('CDR', 'I.E.Concentración DE Desarrollo Rural'),
        ('PLT', 'I.E.Pedro Leon Torres'),
        ('AMY', 'Alcaldia Municipal De Yacuanquer')
    )
    id_transporte=models.OneToOneField(TipoTransporte, on_delete=models.CASCADE, null=True, verbose_name="Lista De Vehiculos")
    institucion=models.CharField("Institución", max_length=5, choices=INSTITUCION_TYPE)
    id_conductor=models.OneToOneField(Conductor, on_delete=models.CASCADE, null=True, verbose_name="Conductores")
    placa=models.CharField("Placa", max_length=7)
    soat_exp=models.DateField("Fecha de Expedición Soat")
    soat_ven=models.DateField("Fecha de Vencimiento Soat")
    poliza_exp=models.DateField("Fecha de Expedición Poliza")
    poliza_ven=models.DateField("Fecha de Vencimiento Poliza")
    tecno_mecanico_exp=models.DateField("Fecha de Expedición Tecnico Mecanico")
    tecno_mecanico_ven=models.DateField("Fecha de Vencimiento Tecnico Mecanico")
    id_mantenimiento=models.ManyToManyField(Mantenimiento)

    class Meta:
        verbose_name = "Registrar Datos Del Vehiculo"
        verbose_name_plural ="Registrar Datos De los Vehiculos"
    def __str__(self):
        return '{0} - {1} - {2}'.format(self.id_transporte,self.institucion,self.placa)        

# Modelo Agenda
class Agenda (models.Model):
  
    id_usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, verbose_name="Lista De Usuarios")
    id_transporte=models.OneToOneField(TipoTransporte, on_delete=models.CASCADE, null=True, verbose_name="Lista De Vehiculos")
    turno_agenda_inicio=models.DateTimeField("Asignar Turno De Inicio")
    turno_agenda_final=models.DateTimeField("Asignar Turno Final")    
    direccion=models.CharField("Dirección", max_length=200)
    costo=models.BigIntegerField("Costo Total")

    class Meta:
        verbose_name = "Registrar Datos Agenda"
        verbose_name_plural ="Registrar Datos En la Agenda"
    def __str__(self):
        return 'Usuario: {0}'.format(self.id_usuario)        

