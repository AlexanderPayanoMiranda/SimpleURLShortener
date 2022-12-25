import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as schema_file:
    connection.executescript(schema_file.read())

connection.commit()
connection.close()
