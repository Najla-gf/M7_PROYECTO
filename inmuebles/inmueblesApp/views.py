from django.shortcuts import render, redirect, get_object_or_404 
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario, Inmueble, Region, Comuna, SolicitudArriendo
from .forms import CrearUsuarioForm, ActualizarUsuarioForm, InmuebleForm, UsuarioForm, SolicitudArriendoForm
from .services import crear_solicitud_arriendo, listar_solicitudes_arriendo_por_arrendador, borrar_solicitud_arriendo


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
            messages.error(request, 'Credenciales incorrectas, intente nuevamente.')
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
    
    regiones = Region.objects.all()
    return render(request, 'agregar_inmueble.html', {'form': form, 'regiones': regiones})

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
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = InmuebleForm(instance=inmueble)
    
    regiones = Region.objects.all()
    comunas = Comuna.objects.filter(region=inmueble.region)  # Filtrar comunas por la región del inmueble
    
    return render(request, 'editar_inmueble.html', {'form': form, 'regiones': regiones, 'comunas': comunas})
    
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

# Vista para obtener comunas por región
def obtener_comunas_por_region(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse({'comunas': list(comunas)})

#Modal para los detalles
def inmueble_detalle_api(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    data = {
        'nombre': inmueble.nombre,
        'descripcion': inmueble.descripcion,
        'direccion': inmueble.direccion,
        'comuna': {'id': inmueble.comuna.id, 'nombre': inmueble.comuna.nombre},
        'region': {'id': inmueble.region.id, 'nombre': inmueble.region.nombre},
        'm2_construidos': inmueble.m2_construidos,
        'm2_totales': inmueble.m2_totales,
        'cantidad_habitaciones': inmueble.cantidad_habitaciones,
        'cantidad_banos': inmueble.cantidad_banos,
        'cantidad_estacionamientos': inmueble.cantidad_estacionamientos,
        'tipo_inmueble': {'id': inmueble.tipo_inmueble.id, 'nombre': inmueble.tipo_inmueble.nombre},
        'arrendador': {'id': inmueble.arrendador.id, 'username': inmueble.arrendador.username},
        'precio_mensual': inmueble.precio_mensual,
    }
    return JsonResponse(data)

#Solicitud de arriendo
@login_required
def solicitud_arriendo_view(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    usuario = get_object_or_404(Usuario, user=request.user)
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data['mensaje']
            crear_solicitud_arriendo(usuario, inmueble, mensaje)
            messages.success(request, 'Solicitud de arriendo enviada con éxito. ¡El arrendador se pondrá en contacto!')
            return redirect('listar_inmuebles')
    else:
        form = SolicitudArriendoForm()
    return render(request, 'solicitud_arriendo.html', {'form': form, 'inmueble': inmueble})

@login_required
def listar_solicitudes_arriendo_view(request):
    arrendador = request.user.usuario
    solicitudes = listar_solicitudes_arriendo_por_arrendador(arrendador)
    return render(request, 'listar_solicitudes_arriendo.html', {'solicitudes': solicitudes})

@login_required
def borrar_solicitud_arriendo_view(request, solicitud_id):
    borrar_solicitud_arriendo(solicitud_id)
    messages.success(request, 'La solicitud de arriendo fue eliminada.')
    return redirect('listar_solicitudes_arriendo')