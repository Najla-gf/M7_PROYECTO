document.addEventListener('DOMContentLoaded', function() {
    var inmuebleModal = document.getElementById('inmuebleModal');
    inmuebleModal.addEventListener('show.bs.modal', function(event) {
        var button = event.relatedTarget;
        var imagen = button.getAttribute('data-imagen');
        var nombre = button.getAttribute('data-nombre');
        var descripcion = button.getAttribute('data-descripcion');
        var direccion = button.getAttribute('data-direccion');
        var comuna = button.getAttribute('data-comuna');
        var region = button.getAttribute('data-region');
        var m2_construidos = button.getAttribute('data-m2-construidos');
        var m2_totales = button.getAttribute('data-m2-totales');
        var habitaciones = button.getAttribute('data-habitaciones');
        var banos = button.getAttribute('data-banos');
        var estacionamientos = button.getAttribute('data-estacionamientos');
        var tipo_inmueble = button.getAttribute('data-tipo-inmueble');
        var arrendador = button.getAttribute('data-arrendador');
        var precio = button.getAttribute('data-precio');

        document.getElementById('modalImagen').src = imagen;
        document.getElementById('modalNombre').textContent = nombre;
        document.getElementById('modalDescripcion').textContent = descripcion;
        document.getElementById('modalDireccion').textContent = direccion;
        document.getElementById('modalComuna').textContent = comuna;
        document.getElementById('modalRegion').textContent = region;
        document.getElementById('modalM2Construidos').textContent = m2_construidos;
        document.getElementById('modalM2Totales').textContent = m2_totales;
        document.getElementById('modalHabitaciones').textContent = habitaciones;
        document.getElementById('modalBanos').textContent = banos;
        document.getElementById('modalEstacionamientos').textContent = estacionamientos;
        document.getElementById('modalTipoInmueble').textContent = tipo_inmueble;
        document.getElementById('modalArrendador').textContent = arrendador;
        document.getElementById('modalPrecioMensual').textContent = precio;
    });
});
