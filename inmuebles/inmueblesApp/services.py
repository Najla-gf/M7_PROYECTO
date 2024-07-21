from django.shortcuts import get_object_or_404
from .models import Usuario, Region, Comuna, TipoInmueble, Inmueble, SolicitudArriendo

# Crear un objeto con el modelo Usuario
def crear_usuario(user, nombres, apellidos, rut, direccion, telefono_personal, correo_electronico, tipo_usuario='arrendatario'):
    usuario = Usuario(
        user=user,
        nombres=nombres,
        apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        telefono_personal=telefono_personal,
        correo_electronico=correo_electronico,
        tipo_usuario=tipo_usuario
    )
    usuario.save()
    return usuario

# Listar todos los usuarios
def listar_usuarios():
    return Usuario.objects.all()

# Actualizar un registro en el modelo Usuario
def actualizar_usuario(usuario_id, **kwargs):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for key, value in kwargs.items():
        setattr(usuario, key, value)
    usuario.save()
    return usuario

# Borrar un registro del modelo Usuario
def borrar_usuario(usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()

# Crear un objeto con el modelo Inmueble
def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_banos, direccion, tipo_inmueble, precio_mensual, arrendador, region, comuna, imagen_url=None):
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_totales=m2_totales,
        cantidad_estacionamientos=cantidad_estacionamientos,
        cantidad_habitaciones=cantidad_habitaciones,
        cantidad_banos=cantidad_banos,
        direccion=direccion,
        tipo_inmueble=tipo_inmueble,
        precio_mensual=precio_mensual,
        arrendador=arrendador,
        region=region,
        comuna=comuna,
        imagen_url=imagen_url
    )
    inmueble.save()
    return inmueble

# Listar todos los inmuebles
def listar_inmuebles():
    return Inmueble.objects.all()

# Actualizar un registro en el modelo Inmueble
def actualizar_inmueble(inmueble_id, **kwargs):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    for key, value in kwargs.items():
        setattr(inmueble, key, value)
    inmueble.save()
    return inmueble

# Borrar un registro del modelo Inmueble
def borrar_inmueble(inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    inmueble.delete()

# Crear una solicitud de arriendo
def crear_solicitud_arriendo(arrendatario, inmueble, mensaje):
    solicitud = SolicitudArriendo(
        arrendatario=arrendatario,
        inmueble=inmueble,
        mensaje=mensaje
    )
    solicitud.save()
    return solicitud

# Listar todas las solicitudes de arriendo para un arrendador específico
def listar_solicitudes_arriendo_por_arrendador(arrendador):
    return SolicitudArriendo.objects.filter(inmueble__arrendador=arrendador)

# Borrar un registro del modelo SolicitudArriendo
def borrar_solicitud_arriendo(solicitud_id):
    solicitud = get_object_or_404(SolicitudArriendo, id=solicitud_id)
    solicitud.delete()

# Actualizar un registro en el modelo SolicitudArriendo
def actualizar_solicitud_arriendo(solicitud_id, **kwargs):
    solicitud = get_object_or_404(SolicitudArriendo, id=solicitud_id)
    for key, value in kwargs.items():
        setattr(solicitud, key, value)
    solicitud.save()
    return solicitud

