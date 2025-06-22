\"\"\"db_utils.py — работа с SQLite для сохранения прогнозов\"\"\"
import sqlite3
from typing import Tuple

def connect_db(db_path: str) -> sqlite3.Connection:
    \"\"\"Возвращает соединение с БД по пути db_path\"\"\"
    conn = sqlite3.connect(db_path)
    return conn

def init_preds_table(conn: sqlite3.Connection) -> None:
    \"\"\"Создаёт таблицу preds, если её нет\"\"\"
    cursor = conn.cursor()
    cursor.execute(\"
        CREATE TABLE IF NOT EXISTS preds(
            ts TEXT PRIMARY KEY,
            exact REAL,
            rounded INTEGER,
            model_ver TEXT
        )
    \")
    conn.commit()

def insert_pred(conn: sqlite3.Connection, ts: str, exact: float, rounded: int, model_ver: str) -> None:
    \"\"\"Вставляет одну запись прогноза\"\"\"
    cursor = conn.cursor()
    cursor.execute(
        'INSERT OR REPLACE INTO preds(ts, exact, rounded, model_ver) VALUES (?, ?, ?, ?)',
        (ts, exact, rounded, model_ver)
    )
    conn.commit()

def get_last_pred(conn: sqlite3.Connection) -> Tuple[str, float, int, str]:
    \"\"\"Возвращает самую свежую запись\"\"\"
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM preds ORDER BY ts DESC LIMIT 1')
    return cursor.fetchone()

if __name__ == "__main__":
    # простой тест
    conn = connect_db("data/predictions.db")
    init_preds_table(conn)
    print("✅ db_utils.py stub: OK")
