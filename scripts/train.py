#!/usr/bin/env python3
"""
train.py — обучает модель на исторических данных и сохраняет её как model.pkl
"""
import os

def main():
    # Проверяем наличие ключа и данных
    api_key = os.getenv("WU_API_KEY")
    if not api_key:
        raise RuntimeError("WU_API_KEY not set")
    # TODO: загрузить данные из data/raw, обучить модель и сохранить model.pkl
    print("✅ train.py stub: OK")

if __name__ == "__main__":
    main()
