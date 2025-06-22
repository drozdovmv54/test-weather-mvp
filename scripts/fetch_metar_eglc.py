#!/usr/bin/env python3
"""
fetch_metar_eglc.py — скачивает последний METAR EGLC с NOAA
и сохраняет его для тренера.
"""
import requests

def main():
    url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/EGLC.TXT"
    resp = requests.get(url)
    resp.raise_for_status()
    print("✅ fetch_metar_eglc.py stub: OK")
    # TODO: сохранить resp.text в нужном месте

if __name__ == "__main__":
    main()
