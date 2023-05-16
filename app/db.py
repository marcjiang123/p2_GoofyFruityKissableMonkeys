"""
GoofyFruityKissableMonkeys
"""

import sqlite3

DB_FILE = "back.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()
#db.execute("DROP TABLE if exists avocadoData")
db.executescript("""
CREATE TABLE if not exists userbase(username text, password text, wins int, losses int, recents text);
CREATE TABLE if not exists avocadoData(date date, avg_price real, total_volume real, small real, medium real, large real, 
total_bags real, small_bags real, large_bags real, xlarge_bags real, type text, year int, geography text);
INSERT into userbase values("avocado","avocado",0,0,"");
""")
c.close()

def user_exists(username): 
    c = db.cursor()
    name = c.execute("Select username from userbase where username = ?", (str(username),))
    exists = name.fetchone() is not None #returns true if user EXISTS
    if exists == None:
        return False
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
    input_pass = c.execute('select password from userbase where (username = ? )', (str(username), )).fetchone()
    # row = c.fetchone()
    if input_pass == None:
        return False
    # input_pass = row[0]
    print(input_pass)
    print(password)
    c.close()
    return password == input_pass[0]

def get_column_names():
    c = db.cursor()
    table = c.execute('select * from avocadoData')
    names = list(map(lambda x: x[0], table.description))
    c.close()
    return names

def populate(csv_contents):
    c = db.cursor()
    c.executemany("insert into avocadoData(date, avg_price, total_volume, small, medium, large, total_bags, small_bags, large_bags, xlarge_bags, type, year, geography) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", csv_contents)
    db.commit()
    c.close()
#def add_data():

def get_date():
    c = db.cursor()
    date_price = c.execute("select date, avg_price from avocadoData").fetchall()
    #print(dates[0][0])
    c.close()
    return date_price

#print(get_date()[0][1]) #prints price

def update_win_lose(username, result):
    c = db.cursor()
    if(result == "win"):
        wins = c.execute("SELECT wins from userbase where (username = ?)", (str(username),))
        c.execute("INSERT into userbase (wins) values(?)", (wins + 1,))
    else:
        losses = c.execute("SELECT losses from userbase where (username = ?)", (str(username),))
        c.execute("INSERT into userbase (losses) values(?)", (losses + 1,))
    db.commit()
    c.close()

def get_price(date):
    c = db.cursor()
    prices = c.execute("SELECT avg_price from avocadoData where date >= ?", (str(date),)).fetchall()
    #print(prices)
    c.close()
    return prices

def get_random_date():
    c = db.cursor()
    date = c.execute("select date from avocadoData order by random() LIMIT 1").fetchone()
    c.close()
    return date[0]

print(get_random_date())

#get_price("2020-11-29")
print(get_price(get_random_date()))
#print("2020-11-29" >= "2020-12-07")