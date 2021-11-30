from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

	imagen = forms.ImageField(required=False)

	class Meta:
		model = Usuario
		fields = ["run", "nombre", "apellido_p", "apellido_m", "tipo_us", "contrasena", "correo"]
		#fields = '__all__'

class DepartamentoForm(forms.ModelForm):
	imagen = forms.ImageField(required=False)
	#mantenimiento_cod_mantenimiento = ForeignKey(required=False)
	#inventario_cod_invetario = ForeignKey(required=False)
	class Meta:
		model = Departamento
		fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields= ["username", "first_name", "last_name", "email", "password1", "password2"]

class ReservaForm(forms.ModelForm):

	class Meta:
		model = Reserva
		fields = '__all__'

class InventarioForm(forms.ModelForm):

	class Meta:
		model = Inventario
		fields = '__all__'