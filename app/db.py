"""
GoofyFruityKissableMonkeys
"""

import sqlite3

DB_FILE = "back.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()
db.executescript("""
CREATE TABLE if not exists userbase(username text, password text, wins int, losses int, recents text);
""")

def user_exists(username): #returns true if user EXISTS
    c = db.cursor()
    name = c.execute("Select user from userbase where user = ?", (username,))
    c.close()
    name.fetchone() is not None 
    
def add_user(username, password):
    c = db.cursor()
    if not user_exists(username):
        c.execute("Insert into userbase values(?,?)", (username, password))
    c.close()

def check_pass(username, password):
    c = db.cursor()
    