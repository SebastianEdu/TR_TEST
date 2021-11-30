from django.urls import path
from .views import *

urlpatterns = [
	path('', home,name="home"),
	#Registrar Usuarios
	path('agregar_cliente/', agregar_cliente, name="agregar_cliente"),
	path('listar_clientes/', listar_clientes, name="listar_clientes"),
	path('modificar_cliente/<run>/', modificar_cliente, name="modificar_cliente"),
	path('eliminar_cliente/<run>/', eliminar_cliente, name="eliminar_cliente"),
	#Departamentos
	path('agregar_departamento/', agregar_departamento, name="agregar_departamento"),
	path('listar_departamentos/', listar_departamentos, name="listar_departamentos"),
	path('modificar_departamento/<cod_depa>/', modificar_departamento, name="modificar_departamento"),
	path('eliminar_departamento/<cod_depa>/', eliminar_departamento, name="eliminar_departamento"),
	#Usuarios-Django
	path('registro/', registro, name="registro"),
	#reservas
	path('agregar_reserva/', agregar_reserva, name="agregar_reserva"),
	path('listar_reservas/', listar_reservas, name="listar_reservas"),
	path('modificar_reserva/<cod_reserva>/', modificar_reserva, name="modificar_reserva"),
	path('eliminar_reserva/<cod_reserva>/', eliminar_reserva, name="eliminar_reserva"),
	#inventario
	path('agregar_inventario/', agregar_inventario, name="agregar_inventario"),
	path('listar_inventarios/', listar_inventarios, name="listar_inventarios"),
	path('modificar_inventario/<cod_inventario>/', modificar_inventario, name="modificar_inventario"),
	path('eliminar_inventario/<cod_inventario>/', eliminar_inventario, name="eliminar_inventario"),

]