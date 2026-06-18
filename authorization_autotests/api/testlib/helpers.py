import hashlib
import json
import os
import random
import re
import string
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from faker import Faker

from api.testlib.const import VKWORKSPACE_DOMAIN

SEPARATORS = "._-"
CHARS = string.ascii_lowercase + string.digits


def _random_login(length: int = 10) -> str:
    if length < 1:
        raise ValueError("length must be >= 1")
    result = []
    for _ in range(length):
        ch = random.choice(CHARS)
        result.append(ch)
    return "".join(result)


def sleep_or_exit(msg: str, iteration: int, tries: int, sleep: int = 10) -> bool:
    if iteration == tries:
        raise

    time.sleep(sleep)
    return True


def generate_email(domain: str, length: int = 10) -> str:
    """Возвращает строку вида username@domain"""
    integer_timestamp = int(time.time())
    username = f"{_random_login(length)}{integer_timestamp}"
    return username, f"{username}@{domain}"


def generate_user_data(password: str, domain: str = VKWORKSPACE_DOMAIN) -> Dict:
    """Хэлпер для генерации данных пользователя перез созданием в biz"""
    login, email = generate_email(domain)
    # Используем Faker для генерации реалистичных имен
    faker = Faker("ru_RU")
    gender = random.choice(["male", "female"])

    if gender == "male":
        first_name = faker.first_name_male()
        last_name = faker.last_name_male()
    else:
        first_name = faker.first_name_female()
        last_name = faker.last_name_female()

    return {
        "email": email,
        "password": password,
        "login": login,
        "gender": gender,
        "domain": domain,
        "firstname": first_name,
        "lastname": last_name,
        "full_name": f"{first_name} {last_name}",
    }


def get_file_hash_and_size(file_path: str) -> Dict:
    """Вычисляет хэш и размер файла"""
    # Получаем размер файла
    file_size = os.path.getsize(file_path)

    # Вычисляем хэш файла
    hasher = hashlib.sha1()  # noqa: S324

    with open(file_path, "rb") as f:
        # Читаем файл блоками для больших файлов
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)

    file_hash = hasher.hexdigest()

    return {"file_hash": file_hash, "file_size": file_size}


def add_minutes(date_string: str, minutes: int, revert: Optional[bool] = False) -> str:
    dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")  # noqa: DTZ007
    if dt.minute < 15:  # noqa: PLR2004
        dt = dt.replace(minute=0, second=0, microsecond=0)
    elif dt.minute < 45:  # noqa: PLR2004
        dt = dt.replace(minute=30, second=0, microsecond=0)
    else:
        dt = dt.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    new_dt = dt - timedelta(minutes=minutes) if revert else dt + timedelta(minutes=minutes)
    return new_dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")


def get_workspace_domains() -> List:
    """Return all used in this workspace cluster domain names as list"""
    domain_names = []
    domain_names.append(VKWORKSPACE_DOMAIN)

    return domain_names


def parse_journalctl_json_output(output: str) -> List:
    """Парсинг вывода journalctl, извлекая JSON объекты"""
    logs = []
    json_pattern = r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}"

    matches = re.findall(json_pattern, output)

    for match in matches:
        try:
            log_entry = json.loads(match)
            logs.append(log_entry)
        except json.JSONDecodeError:
            # Пропускаем некорректные JSON
            continue

    return logs

def generate_string(n):
    s = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    return s