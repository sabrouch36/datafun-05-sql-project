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

##Setup Instructions

Clone the repository:

git clone https://github.com/teflxndxn/datafun-05-sql.git
cd datafun-05-sql


Create and activate a Python virtual environment:

python3 -m venv .venv source .venv/bin/activate # macOS/Linux .venv\Scripts\activate # Windows

Install dependencies:
pip install -r requirements.txt

Run the database setup script to create tables and insert data:
python db01_setup.py

Run the features script to update or delete records:
python sql_features/db02_features.py

Run the query script to see data querying examples:
python sql_queries/db03_queries.py

Database Schema
This project uses two related tables:

products

product_id (Primary Key)

category

price

rating

stock

sales

sale_id (Primary Key)

product_id (Foreign Key to products.product_id)

quantity

sale_date

Foreign key constraints enforce data integrity between products and sales.



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

### Query Result: Sorted Books by Year

![Sorted Books](screenshotsquery_sort_books_result.png)
