let dataTable;

const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileNameDiv = document.getElementById('fileName');

// Клик по dropZone открывает выбор файла
dropZone.addEventListener('click', () => fileInput.click());

// Подсветка при dragover
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.style.background = '#f0f0f0';
});
dropZone.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropZone.style.background = '';
});

// Обработка drop
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.style.background = '';
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
        fileInput.files = e.dataTransfer.files; // Помещаем файл в input
        fileNameDiv.textContent = `File: ${e.dataTransfer.files[0].name}`;
    }
});

// Если файл выбран через input, показываем имя
fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        fileNameDiv.textContent = `File: ${fileInput.files[0].name}`;
    }
});

document.getElementById('uploadForm').onsubmit = function(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение формы
    document.getElementById('loading').style.display = 'block';
    document.getElementById('formContainer').style.display = 'none';

    const fileInput = document.querySelector('input[type="file"]');
    const selectedType = document.getElementById('log_type').value;
    const fileName = fileInput.files[0].name;
    document.getElementById('fileName').textContent = `File: ${fileName}`;

    const formData = new FormData(document.getElementById('uploadForm'));
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        const tableBody = $('#logTable tbody');
        tableBody.empty(); // Очищаем таблицу перед добавлением новых данных

        data.forEach(log => {
            const row = $('<tr>');
            row.append($('<td>').text(log.line_number || ''));
            row.append($('<td>').text(log.time || ''));
            row.append($('<td>').text(log.level || ''));
            row.append($('<td>').text(log.source || ''));
            const messageCell = $('<td class="message">').text(log.message || log.unparsed || '');
            messageCell.one('click', function() {
                $(this).addClass('expanded');
            });
            row.append(messageCell);
            tableBody.append(row);
        });

        if (dataTable) {
            dataTable.destroy();
        }

        dataTable = $('#logTable').DataTable({
            //"autoWidth": false, // Отключаем автоматическую ширину
            //"scrollY": "50vh", // Высота таблицы с вертикальной прокруткой
            //"scrollCollapse": true,
            "paging": true,
            "pageLength": 1000, // Количество строк на странице
            "columnDefs": [
                { "width": "3%", "targets": 0 }, // Ширина для номера строки
                { "width": "5%", "targets": 1 }, // Ширина для времени
                { "width": "4%", "targets": 2 }, // Ширина для времени
                { "width": "10%", "targets": 3 }, // Ширина для источника
                { "width": "70%", "targets": 4 } // Ширина для сообщения
            ]
        });
        
        $('#logTable').show();
        $('#logTable').colResizable({
            liveDrag: true,
            minWidth: 30
        });
        $('#filters').show(); // Показываем фильтры вместе с таблицей
        
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loading').style.display = 'none';
        document.getElementById('formContainer').style.display = 'block';
    });
    
};

document.getElementById('applyFilters').onclick = function() {
    const lineStart = parseInt(document.getElementById('lineStart').value, 10) || 0;
    const lineEnd = parseInt(document.getElementById('lineEnd').value, 10) || Infinity;
    const timeStart = document.getElementById('timeStart').value || '00:00:00';
    const timeEnd = document.getElementById('timeEnd').value || '23:59:59';

    $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
        const lineNumber = parseInt(data[0], 10) || 0;
        const time = (data[1] || '00:00:00').substring(0, 8); // Убираем миллисекунды

        return (lineNumber >= lineStart && lineNumber <= lineEnd) &&
               (time >= timeStart && time <= timeEnd);
    });

    dataTable.draw();
    $.fn.dataTable.ext.search.pop();
};

const btn = document.getElementById('theme-toggle');

// Проверяем сохранённую тему
if(localStorage.getItem('theme') === 'dark') {
  document.body.classList.add('dark-theme');
  btn.textContent = '☀️';
}

btn.addEventListener('click', () => {
  document.body.classList.toggle('dark-theme');
  const isDark = document.body.classList.contains('dark-theme');
  btn.textContent = isDark ? '☀️' : '🌒';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});