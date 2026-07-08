from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

log_pattern_for_desktop = re.compile(
        r'.(?P<time>\d{2}:\d{2}:\d{2}\.\d{3}).\s+'    # Время
        r'(?P<level>[IWED])\s+'                       # Уровень логирования
        r'(?P<source>.+?)\s+'                         # Источник
        r'(?P<line>\d+)\s+'                           # Номер строки
        r'(?P<address>0x[0-9a-f]+)\s+'                # Адрес памяти
        r'(?P<message>.*)'                            # Сообщение
    )

log_pattern_for_ios = re.compile(
    r'(?P<number>\d+)\s+'                             # Номер строки
    r'(?P<time>\d{1,2}:\d{1,2}:\d{1,2}.\d{1,6})\s+'   # Время
    r'(?P<timezone>[-+]\d{2}:\d{2})\s+'               # Часовой пояс
    r'(?P<level>[A-Z]+)\s+'                           # Уровень логирования
    r'(?:(?P<source>[\[][\w\s]+[\]])\s+)?'            # Источник
    r'(?P<message>.*)'                                # Сообщение
)

log_pattern_for_android = re.compile(
    r'(?P<time>\d{2}:\d{2}:\d{2}\.\d{3})\s+'          # Время
    r'(?P<source>[\[][\w\W]+[\]])\s+'                 # Источник
    r'(?P<level>[A-Z]+)\s+'                           # Уровень логирования
    r'(?P<message>.*)'                                # Сообщение
)

def parse_log(log_content, log_type_from_front):
    if log_type_from_front == 'desktop':
        return parse(log_content, log_pattern_for_desktop)
    if log_type_from_front == 'ios':
        return parse(log_content, log_pattern_for_ios)
    if log_type_from_front == 'android':
        return parse(log_content, log_pattern_for_android)
    pass

def parse(log_content, log_type):
    log_pattern = log_type
    logs = []

    for index, line in enumerate(log_content.splitlines(), start=1):
        match = log_pattern.match(line)
        if match:
            log_entry = match.groupdict()
            log_entry['line_number'] = index  # Добавляем номер строки
            logs.append(log_entry)
        else:
            # Добавляем непарсенные строки с номером строки
            logs.append({"line_number": index, "unparsed": line})

    return logs

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        log_type = request.form.get('log_type')
        if file:
            print('файл загружен')
            content = file.read().decode('utf-8')
            parsed_logs = parse_log(content, log_type)
            return jsonify(parsed_logs)
    return render_template('upload_.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,  debug=True)