document.addEventListener('DOMContentLoaded', () => {
    // Obtén el ID de la criptomoneda desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const criptoId = urlParams.get('cripto_id');

    if (criptoId) {
        // Configura la URL para la imagen del gráfico
        const chartImage = document.getElementById('crypto-chart');
        chartImage.src = `/api/crypto/${criptoId}/chart`;
    }
});
