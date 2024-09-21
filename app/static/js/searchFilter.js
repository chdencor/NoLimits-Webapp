// Script para filtrar la tabla según la búsqueda
document.getElementById('search').addEventListener('input', function() {
    var searchTerm = this.value.toLowerCase();
    var rows = document.querySelectorAll('table tbody tr');

    rows.forEach(function(row) {
        var cells = row.querySelectorAll('td');
        var found = Array.from(cells).some(function(cell) {
            return cell.textContent.toLowerCase().includes(searchTerm);
        });

        row.style.display = found ? '' : 'none';
    });
});
