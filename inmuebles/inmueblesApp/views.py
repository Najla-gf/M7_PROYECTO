from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario, Inmueble, Region, Comuna
from .forms import CrearUsuarioForm, ActualizarUsuarioForm, InmuebleForm, UsuarioForm


# INICIO
def index(request):
    return render(request, 'index.html')

# Formulario de registro
def register(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta fue creada con éxito. Ahora puedes iniciar sesión')
            return redirect('login')
    else:
        form = CrearUsuarioForm()
    return render(request, 'register.html', {'form': form})

# Vista del perfil
@login_required
def profile(request):
    usuario = request.user.usuario
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UsuarioForm(instance=usuario)
    
    context = {
        'user': request.user,
        'usuario': usuario,
        'form': form
    }
    
    return render(request, 'profile.html', context)

# Actualizar perfil
@login_required
def edit_profile(request):
    usuario = Usuario.objects.get(user=request.user)
    if request.method == 'POST':
        form = ActualizarUsuarioForm(request.POST, instance=usuario, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado!')
            return redirect('profile')
    else:
        form = ActualizarUsuarioForm(instance=usuario, user=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# Agregar inmueble
@login_required
def agregar_inmueble(request):
    if not request.user.usuario.tipo_usuario == 'arrendador':
        return redirect('index')

    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user.usuario
            inmueble.save()
            messages.success(request, 'Inmueble agregado exitosamente')
            return redirect('mis_inmuebles')
    else:
        form = InmuebleForm()
    
    return render(request, 'agregar_inmueble.html', {'form': form})

@login_required
def mis_inmuebles(request):
    inmuebles = Inmueble.objects.filter(arrendador=request.user.usuario)
    return render(request, 'mis_inmuebles.html', {'inmuebles': inmuebles})

#Editar inmueble
@login_required
def editar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, arrendador=request.user.usuario)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble actualizado exitosamente')
            return redirect('mis_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    
    return render(request, 'editar_inmueble.html', {'form': form})

#Borrar inmueble
@login_required
def borrar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, arrendador=request.user.usuario)
    if request.method == 'POST':
        inmueble.delete()
        messages.success(request, 'Inmueble borrado exitosamente')
        return redirect('mis_inmuebles')
    
    return render(request, 'borrar_inmueble.html', {'inmueble': inmueble})

#Listar inmuebles para arrendatarios
def listar_inmuebles(request):
    inmuebles = Inmueble.objects.filter()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')

    if region_id:
        inmuebles = inmuebles.filter(region_id=region_id)
        comunas = Comuna.objects.filter(region_id=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)

    return render(request, 'listar_inmuebles.html', {'inmuebles': inmuebles, 'regiones': regiones, 'comunas': comunas})

