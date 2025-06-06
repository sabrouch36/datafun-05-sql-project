import sqlite3
from pathlib import Path

def run_sql_script(script_path: str, db_path: str):
    with sqlite3.connect(db_path) as conn:
        with open(script_path, 'r') as file:
            conn.executescript(file.read())

def apply_features():
    base = Path(__file__).parent
    db_path = base / "books_authors.sqlite"
    sql_folder = base / "sql_features"

    run_sql_script(sql_folder / "update_records.sql", db_path)
    run_sql_script(sql_folder / "delete_records.sql", db_path)

    print("✅ Records updated and deleted.")

if __name__ == "__main__":
    apply_features()
