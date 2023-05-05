"""
GoofyFruityKissableMonkeys
"""

import sqlite3

DB_FILE = "back.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()
db.executescript("""
CREATE TABLE if not exists userbase(username text, password text, wins int, losses int, recents text);
""")
c.close()

def user_exists(username): 
    c = db.cursor()
    name = c.execute("Select username from userbase where username = ?", (username,))
    exists = name.fetchone() is not None #returns true if user EXISTS
    c.close()
    return exists

print(user_exists("joe"))
def add_user(username, password):
    c = db.cursor()
    if not user_exists(username):
        c.execute("Insert into userbase values(?,?)", (username, password,))
    c.close()

def check_pass(username, password):
    c = db.cursor()
    c.execute('select password from userbase where (username = ? )', (str(username), ))
    input_pass = c.fetchone()[1]
    c.close()
    return password == input_pass

    