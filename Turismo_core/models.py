# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

 


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)


class CheckInv1(models.Model):
    cod_chek_in = models.CharField(primary_key=True, max_length=60)
    horario = models.DateField()
    documento = models.BinaryField()

    def __str__(self):
    	return self.cod_chek_in



class CheckOut(models.Model):
    cod_check_out = models.CharField(primary_key=True, max_length=6)
    horario = models.DateField()
    documento = models.BinaryField()
    multa = models.BigIntegerField(blank=True, null=True)
    multa_1 = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
    	return self.cod_check_out

 

class Conductor(models.Model):
    cod_conductor = models.CharField(primary_key=True, max_length=6)
    run = models.IntegerField()
    nombre = models.CharField(max_length=15)
    apellido_p = models.CharField(max_length=15)
    apellido_m = models.CharField(max_length=15)
    tipo_licencia = models.CharField(max_length=10)
    cod_transporte = models.CharField(unique=True, max_length=6)
    dv = models.CharField(max_length=1)
    imagen = models.ImageField(upload_to="Conductores", null=True)

    def __str__(self):
    	return self.nombre

   

class Departamento(models.Model):
    cod_depa = models.CharField(primary_key=True, max_length=6)
    fotos = models.BinaryField()
    dormitorios = models.CharField(max_length=10)
    banos = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    valor_depa_xdia = models.BigIntegerField()
    evaluo_inv_total = models.BigIntegerField()
    imagen = models.ImageField(upload_to="Departamentos", null=True)
    mantenimiento_cod_mantenimiento = models.ForeignKey('Mantenimiento', models.DO_NOTHING, db_column='mantenimiento_cod_mantenimiento')
    inventario_cod_invetario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='inventario_cod__invetario')  # Field renamed because it contained more than one '_' in a row.

    def __str__(self):
    	return self.cod_depa

  
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

  
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

   
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

  
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()




class Inventario(models.Model):
    cod_inventario = models.CharField(primary_key=True, db_column='cod__inventario', unique=True, max_length=6)  # Field renamed because it contained more than one '_' in a row.
    nombre_obj = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()
    estado_obj = models.CharField(max_length=50)
    cod_depa = models.CharField(primary_key=False, max_length=6)
    evaluo_obj = models.BigIntegerField()
    tipo_objeto = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
    	return self.nombre_obj

  

class Mantenimiento(models.Model):
    cod_depa = models.CharField(unique=True, max_length=6)
    cod_mantenimiento = models.CharField(primary_key=True, max_length=6)
    reparacion = models.CharField(max_length=50)
    disponiblidad = models.CharField(max_length=2)
    mejora = models.CharField(max_length=50)
    limpieza = models.CharField(max_length=50)

    def __str__(self):
    	return self.cod_depa


class Reserva(models.Model):
    cod_reserva = models.CharField(primary_key=True, max_length=6)
    pago_parcial = models.BigIntegerField()
    tipo_reserva = models.CharField(max_length=50)
    pago_completo = models.BigIntegerField()
    pago_aprobado = models.BooleanField()
    departamento_cod_depa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_cod_depa')
    usuario_run = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_run')
    check_inv2_cod_chek_in = models.ForeignKey(CheckInv1, models.DO_NOTHING, db_column='check_inv2_cod_chek_in',default="")
    check_out_cod_check_out = models.ForeignKey(CheckOut, models.DO_NOTHING, db_column='check_out_cod_check_out')

    def __str__(self):
    	return self.cod_reserva

  

class Servicios(models.Model):
    cod_serv = models.CharField(primary_key=True, max_length=6)
    transporte_cod_transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='transporte_cod_transporte')
    tour_cod_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='tour_cod_tour')
    reserva_cod_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_cod_reserva')

    def __str__(self):
    	return self.cod_serv

  
class Tour(models.Model):
    cod_tour = models.CharField(primary_key=True, max_length=6)
    horario = models.DateField()
    fecha = models.DateField()
    tipo_tour = models.CharField(max_length=10)

    def __str__(self):
    	return self.cod_tour


class Transporte(models.Model):
    cod_transporte = models.CharField(primary_key=True, max_length=6)
    lugar = models.CharField(max_length=50)
    horario = models.DateField()
    desde = models.CharField(max_length=50)
    hasta = models.CharField(max_length=50)
    vehiculo_cod_vehiculo1 = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_cod_vehiculo1')
    conductor_cod_conductor = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='conductor_cod_conductor')

    def __str__(self):
    	return self.cod_transporte

  

class Usuario(models.Model):
    run = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=20)
    apellido_p = models.CharField(max_length=20)
    apellido_m = models.CharField(max_length=50)
    tipo_us = models.BooleanField()
    contrasena = models.CharField(max_length=16)
    correo = models.EmailField(default="asd@ad.cl")

    def __str__(self):
    	return self.nombre




class Vehiculo(models.Model):
    cod_vehiculo = models.CharField(max_length=6)
    tipo_vehiculo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    patente = models.CharField(max_length=6)
    cod_transporte = models.CharField(unique=True, max_length=6)
    cod_vehiculo2 = models.CharField(primary_key=True, max_length=6)

    def __str__(self):
    	return self.cod_vehiculo



class Zona(models.Model):
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    cod_zona = models.CharField(primary_key=True, max_length=6)

    def __str__(self):
    	return self.ciudad

   