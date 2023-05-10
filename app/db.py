"""
GoofyFruityKissableMonkeys
"""

import sqlite3

DB_FILE = "back.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()
db.executescript("""
CREATE TABLE if not exists userbase(username text, password text, wins int, losses int, recents text);
CREATE TABLE if not exists avocadoData(date text, avg_price real, total_volume real, small real, medium real, large real, 
total_bags real, small_bags real, large_bags real, xlarge_bags real, type text, year int, geography text);
""")
c.close()

def user_exists(username): 
    c = db.cursor()
    name = c.execute("Select username from userbase where username = ?", (str(username),))
    exists = name.fetchone() is not None #returns true if user EXISTS
    c.close()
    return exists

#print(user_exists("joe"))

def add_user(username, password):
    c = db.cursor()
    c.execute("Insert into userbase values(?,?,?,?,?)", (str(username), str(password),0,0,""))
    db.commit()
    c.close()

def check_pass(username, password):
    c = db.cursor()
    c.execute('select password from userbase where (username = ? )', (str(username), ))
    input_pass = c.fetchone()[0]
    c.close()
    return password == input_pass

def get_column_names():
    c = db.cursor()
    table = c.execute('select * from avocadoData')
    names = list(map(lambda x: x[0], table.description))
    c.close()
    return names

def table_insert(column, value):
    c = db.cursor() 
    c.execute(f'INSERT into avocadoData({column}) values(?)', value)
    db.commit()
    c.close()

#table_insert("date",10/10/10)

#def add_data():
