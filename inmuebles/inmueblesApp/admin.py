from django.contrib import admin
from .models import Usuario, Region, Comuna, TipoInmueble, Inmueble, SolicitudArriendo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoInmueble)
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)