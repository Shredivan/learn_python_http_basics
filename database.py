import sqlite3

# Connect to database
# SQL will create this database if doesn't exist
connection = sqlite3.connect('test.db')

# Create cursor
crsr = connection.cursor()

def create_table():
    crsr.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    crsr.execute("INSERT INTO stuffToPlot VALUES(1234, '2016-01-01', 'Python', 5)")
    connection.commit()
    crsr.close()
    connection.close()

create_table()
data_entry()