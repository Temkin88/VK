# Добавляет строки из file1.csv в file2.csv, пропуская дубликаты.
# Результат перезаписывает file2.csv (предварительно делает бэкап file2.csv.bak).

import csv
import shutil
from pathlib import Path

IN1 = Path("17042026 AQA+QA без Silent-сквозной в VKTI по списку.csv")
IN2 = Path("exclusion_4 (1) (2) (1) (1) (1).csv")          # будет обновлён
BACKUP = IN2.with_suffix(IN2.suffix + ".bak")

ENC = "utf-8-sig"                # поменяй на "cp1251", если файлы в Windows-1251
ERRORS = "replace"               # чтобы не падать на битых символах

HAS_HEADER = False               # True, если в CSV есть заголовок в первой строке

def norm_row(row):
    # нормализация для сравнения (чтобы "abc " и "abc" считались одинаковыми)
    return tuple(cell.strip() for cell in row)

def read_rows(path: Path):
    with path.open("r", encoding=ENC, errors=ERRORS, newline="") as f:
        r = csv.reader(f)
        rows = list(r)
    if HAS_HEADER and rows:
        return rows[0], rows[1:]
    return None, rows

def write_rows(path: Path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        w.writerows(rows)

def main():
    h1, rows1 = read_rows(IN1)
    h2, rows2 = read_rows(IN2)

    # Если есть заголовки, считаем что они должны совпадать; берём заголовок из file2
    header = h2 if HAS_HEADER else None

    seen = {norm_row(r) for r in rows2 if r}  # что уже есть в file2
    out_rows = list(rows2)

    added = 0
    for r in rows1:
        if not r:
            continue
        k = norm_row(r)
        if k not in seen:
            seen.add(k)
            out_rows.append(r)
            added += 1

    # бэкап и перезапись file2.csv
    shutil.copy2(IN2, BACKUP)
    write_rows(IN2, header, out_rows)

    print(f"Готово. Добавлено строк: {added}")
    print(f"file2.csv обновлён, бэкап: {BACKUP}")

if __name__ == "__main__":
    main()