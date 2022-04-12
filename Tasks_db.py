import sqlite3

# creating the database
conn = sqlite3.connect("Tasks.db")
# creating a cursor
cursor = conn.cursor()
# create table
cursor.execute("""CREATE TABLE tasks (
    tasks text,
    start_date text,
    colleagues text,
    status text )
    """)

conn.commit()
conn.close()