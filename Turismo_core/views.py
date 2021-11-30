from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def home(request):
    return render(request, "Turismo_core/home.html")

#CRUD reservas
@login_required
def agregar_reserva(request):

	data = {
		'form': ReservaForm()
	}
	if request.method == 'POST':
		formulario = ReservaForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, "Reserva Creada Exitosamente")
		else:
			data["form"] = formulario
	return render(request, "Turismo_core/Reserva/agregar.html", data)

@permission_required('Turismo_core.add_reserva')
def listar_reservas(request):
	reservas = Reserva.objects.all()

	data = {
		'reservas' : reservas
	}
	return render(request, 'Turismo_core/Reserva/listar.html', data)

@permission_required('Turismo_core.change_reserva')
def modificar_reserva(request, cod_reserva):
	reserva = get_object_or_404(Reserva, cod_reserva=cod_reserva)

	data = {
		'form' : ReservaForm(instance=reserva)
	}

	if request.method == 'POST':
		formulario = ReservaForm(data=request.POST, instance=reserva)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, "Reserva Actualizada Exitosamente")
			return redirect(to="listar_reservas")
		data["form"] = formulario
	return render(request, 'Turismo_core/Reserva/modificar.html', data)

@permission_required('Turismo_core.delete_reserva')
def eliminar_reserva(request, cod_reserva):
	reserva = get_object_or_404(Reserva, cod_reserva=cod_reserva)
	reserva.delete()
	messages.success(request, "Reserva Eliminada Exitosamente")
	return redirect(to="listar_reservas")

#usuarios/clientes
def agregar_cliente(request):
	#data = {
	#	'departamentos':departamentos
	#}
	data ={
    	'form':UsuarioForm()
	}

	if request.method == 'POST':
		formulario = UsuarioForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "contacto guardado"
			messages.success(request, "Registrado Exitosamente")
		else:
			data["form"] = formulario

	return render(request, "Turismo_core/Clientes/agregar.html", data)

@permission_required('Turismo_core.view_cliente')
def listar_clientes(request):

	clientes = Usuario.objects.all()

	data = {
		'clientes' : clientes
	}
	return render(request, 'Turismo_core/Clientes/listar.html', data)

@permission_required('Turismo_core.change_cliente')
def modificar_cliente(request, run):
	cliente = get_object_or_404(Usuario, run=run)

	data = {
		'form': UsuarioForm(instance=cliente)
	}

	if request.method == 'POST':
		formulario = UsuarioForm(data=request.POST, instance=cliente, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, "Cliente modificado Exitosamente")
			return redirect(to="listar_clientes")
		data["form"] = formulario
	return render(request, 'Turismo_core/Clientes/modificar.html', data)

@permission_required('Turismo_core.delete_usuario')
def eliminar_cliente(request, run):
	cliente = get_object_or_404(Usuario, run=run)
	cliente.delete()
	messages.success(request, "Cliente Eliminado Exitosamente")
	return redirect(to="listar_clientes")


#CRUD departmentos
@permission_required('Turismo_core.add_departamento')
def agregar_departamento(request):

	data = {
		'form': DepartamentoForm()
	}

	if request.method == 'POST':
		formulario = DepartamentoForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "Departamento Guardado"
			messages.success(request, "Departamento agregado Exitosamente")
			return redirect(to="listar_departamentos")
		else:
			data["form"] = formulario
	return render(request, 'Turismo_core/Departamento/agregar.html', data)

@permission_required('Turismo_core.view_departamento')
def listar_departamentos(request):

	departamentos = Departamento.objects.all()

	data = {
		'departamentos' : departamentos
	}
	return render(request, 'Turismo_core/Departamento/listar.html', data)

@permission_required('Turismo_core.change_departamento')
def modificar_departamento(request, cod_depa):
	departamento = get_object_or_404(Departamento, cod_depa=cod_depa)

	data = {
		'form': DepartamentoForm(instance=departamento)
	}

	if request.method == 'POST':
		formulario = DepartamentoForm(data=request.POST, instance=departamento, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, "Departamento modificado Exitosamente")
			return redirect(to="listar_departamentos")
		data["form"] = formulario
	return render(request, 'Turismo_core/departamento/modificar.html', data)

@permission_required('Turismo_core.delete_departamento')
def eliminar_departamento(request, cod_depa):
	departamento = get_object_or_404(Departamento, cod_depa=cod_depa)
	departamento.delete()
	messages.success(request, "Departamento Eliminado Exitosamente")
	return redirect(to="listar_departamentos")

#Usuarios-django
def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}

	if request.method == 'POST':
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"] )
			login(request, user)
			messages.success(request, "Has ingresado exitosamente")
			return redirect(to="home")
		data["form"] = formulario
	return render(request, 'registration/registro.html', data)

#CRUD Inventario
@permission_required('Turismo_core.add_inventario')
def agregar_inventario(request):

	data = {
		'form': InventarioForm()
	}

	if request.method == 'POST':
		formulario = InventarioForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "Departamento Guardado"
			messages.success(request, "Inventario agregado Exitosamente")
			return redirect(to="listar_inventarios")
		else:
			data["form"] = formulario
	return render(request, 'Turismo_core/Inventario/agregar.html', data)

@permission_required('Turismo_core.view_inventario')
def listar_inventarios(request):

	inventarios = Inventario.objects.all()

	data = {
		'inventarios' : inventarios
	}
	return render(request, 'Turismo_core/Inventario/listar.html', data)

@permission_required('Turismo_core.change_inventario')
def modificar_inventario(request, cod_inventario):
	inventario = get_object_or_404(Inventario, cod_inventario=cod_inventario)

	data = {
		'form': InventarioForm(instance=inventario)
	}

	if request.method == 'POST':
		formulario = InventarioForm(data=request.POST, instance=inventario, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, "Invenario modificado Exitosamente")
			return redirect(to="listar_inventarios")
		data["form"] = formulario
	return render(request, 'Turismo_core/Inventario/modificar.html', data)

@permission_required('Turismo_core.delete_inventario')
def eliminar_inventario(request, cod_inventario):
	inventario = get_object_or_404(Inventario, cod_inventario=cod_inventario)
	inventario.delete()
	messages.success(request, "Inventario Eliminado Exitosamente")
	return redirect(to="listar_inventarios")
