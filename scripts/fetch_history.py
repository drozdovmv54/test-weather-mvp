#!/usr/bin/env python3
"""
fetch_history.py — скачивает 4 недели данных:
• METAR EGLC (NOAA)
• Погодные данные ILONDO575 (WU API)
Сохраняет их в data/raw/*.parquet
"""
import os

def main():
    api_key = os.getenv("WU_API_KEY")
    if not api_key:
        raise RuntimeError("WU_API_KEY not set")
    # TODO: реализовать логику загрузки и сохранения в Parquet
    print("✅ fetch_history.py stub: OK")

if __name__ == "__main__":
    main()
