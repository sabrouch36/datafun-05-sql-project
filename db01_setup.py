import sqlite3
from pathlib import Path

def run_sql_script(script_path: str, db_path: str):
    with sqlite3.connect(db_path) as conn:
        with open(script_path, 'r') as file:
            conn.executescript(file.read())

def setup_database():
    base = Path(__file__).parent
    db_path = base / "books_authors.sqlite"
    sql_folder = base / "sql_create"

    run_sql_script(sql_folder / "01_drop_tables.sql", db_path)
    run_sql_script(sql_folder / "02_create_tables.sql", db_path)
    run_sql_script(sql_folder / "03_insert_records.sql", db_path)

    print("✅ Database created and populated.")

if __name__ == "__main__":
    setup_database()
