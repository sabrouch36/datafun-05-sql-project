from pathlib import Path
import sqlite3

def run_and_print_query(script_path: Path, db_path: Path):
    with sqlite3.connect(db_path) as conn:
        with open(script_path, 'r') as file:
            query = file.read()
            cursor = conn.cursor()
            print(f"\n🔍 Running query from: {script_path.name}\n{'-'*40}")
            for result in cursor.execute(query):
                print(result)

def run_queries():
    base = Path(__file__).parent
    db_path = base / "books_authors.sqlite"
    sql_folder = base / "sql_queries"

    for script in sql_folder.glob("*.sql"):
        if "aggregation" in script.name:
            continue  # skip multi-statement files
        run_and_print_query(script, db_path)

if __name__ == "__main__":
    run_queries()
