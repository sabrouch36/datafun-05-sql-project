# datafun-05-sql-project
This project integrates Python and SQL using SQLite. It involves schema design, data insertion, and querying using SQL and Python.

## 🗂️ Project Structure
datafun-05-sql-project/
│
├── books_authors.sqlite # The SQLite database
├── sql_create/ # SQL scripts to create and populate database
│ ├── 01_drop_tables.sql
│ ├── 02_create_tables.sql
│ └── 03_insert_records.sql
├── sql_features/ # SQL scripts to update and delete records
│ ├── update_records.sql
│ └── delete_records.sql
├── sql_queries/ # SQL queries for analysis
│ ├── query_count_books.sql
│ ├── query_avg_year.sql
│ ├── query_filter_old_books.sql
│ ├── query_sort_books.sql
│ ├── query_group_by_author.sql
│ └── query_join_authors_books.sql
├── db01_setup.py # Runs SQL create scripts
├── db02_features.py # Runs update/delete SQL scripts
├── db03_queries.py # Executes all SQL query scripts
└── README.md # Project report



---

##  How to Run

Make sure your virtual environment is activated, then run the Python scripts in order:

```bash
python db01_setup.py       # Creates the database and inserts records
python db02_features.py    # Updates and deletes records
python db03_queries.py     # Runs analytical queries and prints results

 Features
- SQL table creation with foreign keys

- Data population using raw SQL

- Update & delete records via SQL

- SQL queries: filtering, sorting, aggregation, joins

- Python integration using sqlite3 and pathlib

