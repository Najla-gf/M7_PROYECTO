import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmuebles.settings')
django.setup()

from inmueblesApp.models import Inmueble, Comuna, Region

def consultar_inmuebles_por_comuna():
    with open('Hito2/inmuebles_por_comuna.txt', 'w', encoding='utf-8') as f:
        f.write("Listado de Inmuebles por Comuna:\n\n")
        
        comunas = Comuna.objects.filter(inmueble__isnull=False).distinct()
        for comuna in comunas:
            f.write(f"Comuna: {comuna.nombre}\n")
            inmuebles = Inmueble.objects.filter(comuna=comuna).only('nombre', 'descripcion')
            for inmueble in inmuebles:
                f.write(f"Nombre: {inmueble.nombre}\n")
                f.write(f"Descripción: {inmueble.descripcion}\n\n")

def consultar_inmuebles_por_region():
    with open('Hito2/inmuebles_por_region.txt', 'w', encoding='utf-8') as f:
        f.write("Listado de Inmuebles por Región:\n\n")
        
        regiones = Region.objects.filter(inmueble__isnull=False).distinct()
        for region in regiones:
            f.write(f"Región: {region.nombre}\n")
            inmuebles = Inmueble.objects.filter(region=region).only('nombre', 'descripcion')
            for inmueble in inmuebles:
                f.write(f"Nombre: {inmueble.nombre}\n")
                f.write(f"Descripción: {inmueble.descripcion}\n\n")

if __name__ == "__main__":
    consultar_inmuebles_por_comuna()
    consultar_inmuebles_por_region()
