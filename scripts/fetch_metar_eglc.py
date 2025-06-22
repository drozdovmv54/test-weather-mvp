#!/usr/bin/env python3
"""
fetch_metar_eglc.py — скачивает последний METAR EGLC с минимальной задержкой
(через ~5 мин после съёмки) и сохраняет результат в data/raw/metar_latest.csv
для скрипта trainer.py.
"""
import os
import requests
import csv
from datetime import datetime

def parse_metar(text: str):
    lines = [l for l in text.strip().splitlines() if l.startswith("EGLC")]
    if not lines:
        raise RuntimeError("No EGLC METAR found")
    parts = lines[-1].split()

    # Сборка UTC-timestamp
    day = text.strip().splitlines()[0].split()[0]  # YYYY-MM-DD
    ts_part = parts[1]                            # e.g. '220920Z'
    hh, mm = ts_part[2:4], ts_part[4:6]
    ts = f"{day}T{hh}:{mm}:00Z"

    # Ищем часть с температурой (первую, в которой есть '/')
    temp_group = next((p for p in parts if '/' in p), None)
    if temp_group is None:
        raise RuntimeError("Temperature group not found")
    # извлекаем первую часть до '/' и конвертим в float
    temp_c = float(temp_group.split('/')[0].lstrip('M').replace('M', '-'))
    return ts, temp_c

def main():
    url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/EGLC.TXT"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    ts, temp = parse_metar(r.text)

    os.makedirs("data/raw", exist_ok=True)
    out_path = "data/raw/metar_latest.csv"
    write_header = not os.path.exists(out_path)
    with open(out_path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["ts", "temp_c"])
        writer.writerow([ts, temp])

    print(f"✅ fetch_metar_eglc: saved latest METAR @ {ts} → {temp}°C")
    
if __name__ == "__main__":
    main()
