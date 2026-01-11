### SQL BASIC ###
# From Python 3.9, it supports the SQLite (RDBMS) -> we do not need to install it like (PostgreSQL, or SQLServer, or Oracle)
# We can call "sqlite3" in command line
import sqlite3

#conn = sqlite3.connect("company.db") # create/or connect a database named "company"

# SQLite is supper small/lite (They do not need server) -> just need a file of .db (so client application can interact with database inside itself)
# How it works?
# Python App/Dbeaver -> sqlite module -> SQLite Clibrary -> .db file on disk
# No server, so sockets
# SQLite has no server-client system (serve many users over a network, i.e. whole company), 
# SQLite just as an embedded database (give app a reliable database inside itself)
# No ports, no users/passwords, no admin role
# Where to find ?: Mobile apps (shipped with SQLite, spotify offline playlists, Zalo message catche), Desktop apps (password managers, media libraries), IoT devices
# DataML workflow: local experiement results, small datasets, light ETL, where Excel/SQL are too messy for demo
# SQLite does not need management tool to interact with (like SSMS for SQLServer, pgAdmin for PostgreSQL), you can use Python to interact and write query

# SQLite: data stored only file.db (database is a single file)
# SQLSErver: data stored in (.mdf (primary data), .ndf (secondary), .ldf (log transaction)) (database is a service that manages many files)

### SQLite with Python ###
# I have used "dbeaver" to create table with columns, then insert several records in table"
###
# CREATE TABLE employees (
# 	id INT PRIMARY KEY,
# 	name VARCHAR(50),
# 	department VARCHAR(50),
# 	salary INT,
# 	hire_date DATE
# );

# INSERT INTO employees (id, name, department, salary, hire_date) VALUES
# (1, 'Alice', 'HR', 50000, '2019-03-15'),
# (2, 'Bob', 'IT', 12434, '2019-01-16'),
# (3, 'Charlie', 'IT', 65000, '2018-03-01'),
# (4, 'David', 'Finance', 45000, '2017-01-01');
### Now we can use Python to write querry like in "SSMS, PgAdmin, dbeaver"

# Create or connect to database [Connection object] -> database connection
# conn = sqlite3.connect("company.db")
# Create a cursor object [Cursor object] -> execute sql query
# cur = conn.cursor()
# Context manager {with ....} (close when program is done to prevent leaking data), close code automatically 
with sqlite3.connect("company.db") as conn: # with... (context manager), .connect() {connect or create database}
    # Using with... allow to automatically close database when getting out of blockcode
    cur = conn.cursor() # cursor object to execute query
    # We are still in the query mode, database is still open (...with)
    # Create table with columns
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
	        id INT PRIMARY KEY,
	        name VARCHAR(50),
	        department VARCHAR(50),
	        salary INT,
	        hire_date DATE)
                """)
    # Create a list of data to insert into table
    employees = [
        (1, 'Alice', 'HR', 50000, '2019-03-15'),
        (2, 'Bob', 'IT', 12434, '2019-01-16'),
        (3, 'Charlie', 'IT', 65000, '2018-03-01'),
        (4, 'David', 'Finance', 45000, '2017-01-01')
    ]
    cur.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees
    ) 

    # End context manager -> database (company.db) is closed automatically

# Limitation: the above writting query code using STRING with python library (Very difficult to debug)

### ORM ### SQLAlchemy Engine
### Object Relational Mapping (bridge between OOP and databases) - Write Python Code (Not SQL query anymore)
# Benefits: SQL will be different in (SQLserver, Postgres, ...), then if we execute using Python programs, and if we want to change database in furture, all code syntax will need to change
# If we use ORM, we do not have to 

# The SQLAlchemy support Python 3.9 -> we need to create another env
# conda create -n database_env python=3.9 -y



