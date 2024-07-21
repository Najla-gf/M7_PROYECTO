document.addEventListener('DOMContentLoaded', function () {
        var inmuebleModal = document.getElementById('inmuebleModal')
        inmuebleModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget
            var modal = this
            modal.querySelector('#modalImagen').src = button.getAttribute('data-imagen')
            modal.querySelector('#modalNombre').textContent = button.getAttribute('data-nombre')
            modal.querySelector('#modalDescripcion').textContent = button.getAttribute('data-descripcion')
            modal.querySelector('#modalDireccion').textContent = button.getAttribute('data-direccion')
            modal.querySelector('#modalComuna').textContent = button.getAttribute('data-comuna')
            modal.querySelector('#modalRegion').textContent = button.getAttribute('data-region')
            modal.querySelector('#modalM2Construidos').textContent = button.getAttribute('data-m2-construidos')
            modal.querySelector('#modalM2Totales').textContent = button.getAttribute('data-m2-totales')
            modal.querySelector('#modalHabitaciones').textContent = button.getAttribute('data-habitaciones')
            modal.querySelector('#modalBanos').textContent = button.getAttribute('data-banos')
            modal.querySelector('#modalEstacionamientos').textContent = button.getAttribute('data-estacionamientos')
            modal.querySelector('#modalTipoInmueble').textContent = button.getAttribute('data-tipo-inmueble')
            modal.querySelector('#modalArrendador').textContent = button.getAttribute('data-arrendador')
            modal.querySelector('#modalPrecioMensual').textContent = button.getAttribute('data-precio')
        })
});

