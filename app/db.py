"""
GoofyFruityKissableMonkeys
"""

import sqlite3

DB_FILE = "back.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()
#db.execute("DROP TABLE if exists avocadoData")
db.executescript("""
DROP TABLE if exists userbase;
CREATE TABLE if not exists userbase(username text, password text, wins int, losses int, recents text);
CREATE TABLE if not exists avocadoData(date date, avg_price real, total_volume real, small real, medium real, large real, 
total_bags real, small_bags real, large_bags real, xlarge_bags real, type text, year int, geography text);
CREATE TABLE if not exists stonks(ticker text, company_name text, short_name text, industry text, description text, website text, logo text,
ceo text, exchange text, market_cap int);
INSERT into userbase values("avocado","avocado",0,0,"[]");
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
        c.execute("INSERT into userbase (wins) values(?) where (username = ?)", (wins + 1, str(username)))
    else:
        losses = c.execute("SELECT losses from userbase where (username = ?)", (str(username),))
        c.execute("INSERT into userbase (losses) values(?) where (username = ?)", (losses + 1, str(username)))
    db.commit()
    c.close()

def get_price(date):
    c = db.cursor()
    prices = c.execute("SELECT date, avg_price from avocadoData where date >= ?", (str(date),)).fetchall()
    #print(prices)
    c.close()
    return prices

def get_random_date():
    c = db.cursor()
    date = c.execute("select date from avocadoData order by random() LIMIT 1 ").fetchone()
    c.close()
    return date[0]

#print(get_random_date())

#get_price("2020-11-29")
#print(get_price(get_random_date())[0][0]) #gets one price
#print("2020-11-29" >= "2020-12-07")

def update_recents(username, search):
    c = db.cursor()
    recents = c.execute("SELECT recents from userbase where (username = ?)", (str(username),)).fetchone()
    list = recents[0]
    list.insert(0,search)
    if (len(list) > 5):
        list.pop(5)
    c.execute("INSERT into userbase(recents) values(?) where (username = ?)", (list, str(username)))
    db.commit()
    c.close()

#update_recents("avocado", "blob")
#list = []
#list.append("blob")
#print(list)

def geography_sort(location, convention):
    c = db.cursor()
    date_price = c.execute("SELECT date, avg_price, total_volume, small_bags, medium_bags, large_bags from avocadoData WHERE (geography = ?) AND (type = ?)", (str(location), str(convention))).fetchall()
    c.close()
    return date_price

def get_next_date(date):
    c = db.cursor()
    next_date = c.execute("SELECT date from avocadoData WHERE date > ? order by date asc limit 1", (str(date),)).fetchone()
    c.close()
    return next_date[0]

def get_start_date(date):
    start_year = date.split("-")[0] 
    start_month = str(int(date.split("-")[1]) - 6)
    if int(start_month) < 0:
        start_month = str(int(start_month) + 12)
        start_year = str(int(start_year) - 1)
    if len(start_month) == 1:
        start_month = "0" + start_month
    start_date = start_year + "-" + start_month + "-" + str(int(date.split("-")[2]) - 1)
    start_date = get_next_date(start_date)
    return start_date

def get_price_range(date, location, type):
    c = db.cursor()
    valid = True
    start_date = get_start_date(date)
    compare_date = start_date
    compare_price = c.execute("SELECT avg_price from avocadoData WHERE (date = ?) AND (geography = ?) AND (type = ?)", (str(compare_date),location,type)).fetchone()[0]
    price_change = {}
    while valid:
        price = c.execute("SELECT avg_price from avocadoData WHERE (date = ?) AND (geography = ?) AND (type = ?)", (str(start_date),location,type)).fetchone()
        price_change[start_date] = price[0] / compare_price
        start_date = get_next_date(start_date)
        print(start_date)
        if start_date == date:
            valid = False
    c.close()
    return price_change

def get_all_volume(location,type):
    c = db.cursor()
    start_date = get_start_date(get_start_date("2020-11-29"))
    valid = True
    volume = {}
    while valid:
        if start_date == None:
            valid = False
        print(str(start_date), location, type)
        prices = c.execute("SELECT total_volume from avocadoData WHERE (date = ?) AND (geography = ?) AND (type = ?)", (str(start_date),location,type)).fetchone()
        if prices:
            volume[start_date] = prices[0]
            start_date = get_next_date(start_date)
        else:
            break
    return volume

def get_volume_years(location,type):
    c = db.cursor()
    start_date = "2015-01-04"
    start_year = start_date.split("-")[0]
    valid = True
    volume = {}
    yearSum = 0
    while valid:
        yearSum += c.execute("SELECT total_volume from avocadoData WHERE (date = ?) AND (geography = ?) AND (type = ?)", (str(start_date),location,type)).fetchone()[0]
        if get_next_date(start_date).split("-")[0] != start_year:
            volume[start_year] = yearSum
            yearSum = 0
            start_year = get_next_date(start_date).split("-")[0]
        start_date = get_next_date(start_date)
        if start_date == None:
            valid = False
    return volume

def get_bags(location,type):
    c = db.cursor()
    start_date = "2015-01-04"
    valid = True
    bags = [{},{},{}]
    while valid:
        query = c.execute("SELECT small_bags, medium_bags, large_bags from avocadoData WHERE (date = ?) AND (geography = ?) AND (type = ?)", (str(start_date),location,type)).fetchone()
        bags[0][start_date] = query[0]
        bags[1][start_date] = query[1]
        bags[2][start_date] = query[2]
        start_date = get_next_date(start_date)
        if start_date == None:
            valid = False
    return bags

def get_random_location():
    c = db.cursor()
    location = c.execute("select geography from avocadoData order by random() LIMIT 1 ").fetchone()
    c.close()
    return location[0]

def get_leaderboard():
    c = db.cursor()
    values = c.execute("SELECT username, wins, losses from userbase ORDER by wins DESC").fetchall()
    c.close()
    return values

#print(get_leaderboard())

def get_location_all():
    c = db.cursor()
    location = c.execute("select geography from avocadoData").fetchall()
    c.close()
    return location