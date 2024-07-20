document.getElementById('region').addEventListener('change', function() {
    var regionId = this.value;
    var comunaSelect = document.getElementById('comuna');
    comunaSelect.innerHTML = '<option value="">Todas las comunas</option>'; // Reset options

    if (regionId) {
        fetch(`/api/comunas/?region_id=${regionId}`)
        .then(response => response.json())
        .then(data => {
            data.comunas.forEach(comuna => {
                var option = document.createElement('option');
                option.value = comuna.id;
                option.text = comuna.nombre;
                comunaSelect.add(option);
            });
        });
    }
});
