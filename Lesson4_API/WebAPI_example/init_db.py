import sqlite3
# Database sqlite name:
DATABASE = "employees.db"
# Data to be inserted to database "employees"
# Sample data
sample_data = [
    (1, 'Alice',   'HR',        50000, '2019-03-15'),
    (2, 'Bob',     'IT',        70000, '2020-06-01'),
    (3, 'Charlie', 'IT',        65000, '2018-08-20'),
    (4, 'David',   'Finance',   60000, '2021-01-10'),
    (5, 'Eva',     'HR',        52000, '2017-12-05'),
    (6, 'Frank',   'IT',        68000, '2023-02-12'),
    (7, 'Grace',   'Finance',   61000, '2022-09-18'),
    (8, 'Helen',   'Marketing', 54000, '2020-11-23'),
    (9, 'Ivan',    'Marketing', 57000, '2021-07-30'),
    (10, 'Jack',   'HR',        51000, '2016-10-10')
]
# Create function to interact with database using sqlite3 library in PYthon
def init_db():
    conn = sqlite3.connect(DATABASE) # Connect to database, if database has not existed, it will create one
    cursor = conn.cursor()

    # Drop table if exists (optional for development)
    cursor.execute("DROP TABLE IF EXISTS employees") # This will reset data everytime we run
    # Create table and its schema
    cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER,
        hire_date DATE
    )
    """)

    # Insert data
    cursor.executemany("""
    INSERT INTO employees (id, name, department, salary, hire_date)
    VALUES (?, ?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close() # close the cursor
    print("Database initialized with sample data.")

if __name__ == "__main__":
    init_db()