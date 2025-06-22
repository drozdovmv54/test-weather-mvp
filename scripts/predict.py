#!/usr/bin/env python3
"""
predict.py — берёт модель (пока stub), делает прогноз и сохраняет в SQLite.
"""
import os
import datetime
from db_utils import connect_db, init_preds_table, insert_pred

def main():
    # Параметры
    db_path = os.getenv("DB_PATH", "data/predictions.db")
    conn = connect_db(db_path)
    init_preds_table(conn)

    # TODO: здесь загрузить модель и признаки ILONDO575 + METAR
    # Для MVP пока stub-прогноз:
    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    exact = 0.0
    rounded = int(round(exact))
    model_ver = "stub"

    insert_pred(conn, now, exact, rounded, model_ver)
    print(f"✅ predict: inserted stub @ {now} (exact={exact}, rounded={rounded})")

if __name__ == "__main__":
    main()
