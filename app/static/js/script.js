document.addEventListener('DOMContentLoaded', function() {
    // Obtener el ID de la criptomoneda desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const criptoId = urlParams.get('cripto_id');

    // Construir la URL para obtener el gráfico
    const chartUrl = `/api/crypto/${criptoId}/chart`;

    // Obtener el elemento de la imagen y actualizarlo
    const chartImg = document.getElementById('crypto-chart');
    if (chartImg) {
        chartImg.src = chartUrl;
    }
});
