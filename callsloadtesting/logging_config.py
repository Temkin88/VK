import logging
import os
from datetime import datetime

# Создадим папку logs, если её нет
os.makedirs("/logs", exist_ok=True)

# Получаем текущее время для имени файла
log_filename = datetime.now().strftime("/logs/locust_%Y-%m-%d_%H-%M-%S.log")

# Создадим логгер
logger = logging.getLogger("locust_test")
logger.setLevel(logging.INFO)  # Можно менять уровень (DEBUG, INFO, WARNING и т. д.)

# Формат логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Файловый обработчик
file_handler = logging.FileHandler(log_filename, mode="a")
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

# Логируем, что логирование настроено
logger.info("[TEST] - Начало теста")