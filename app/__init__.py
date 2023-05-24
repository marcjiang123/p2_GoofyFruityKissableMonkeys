# make this neater later
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from stocksymbol import StockSymbol
import db
import random
import requests
import os
import json
import pandas as pd
import yfinance as yf

app = Flask(__name__)
app.secret_key = "hjakdskajsdflkasjdflid"

ss = StockSymbol('9625612b-526c-4289-af96-076826ab74a2')
symbol_list = ss.get_symbol_list(index='SPX')

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def index():
    if 'username' in session:

        date = "2015-01-04"
        start_date = db.get_start_date(date)

        while 1:
            if date.split("-")[0] == "2015" and (int(date.split("-")[1]) < 7):
                date = db.get_random_date()
            else:
                break
        print(date)

        location = "Houston"
        avo_type = "organic"

        beginning_date = start_date

        if request.method == "POST":
            print("HELLO Faiza")

            requestDict = request.form['json']
            requestDict = json.loads(requestDict)


            location = requestDict["place"]
            avo_type = requestDict['convention']

            avo_data = json.dumps(db.get_price_range(date,location,avo_type))
            #avo_vol = json.dumps(db.get_all_volume(location,avo_type))
            print("HELLO???")
            print(avo_data)

            return jsonify(loc=location, avoType=avo_type, avoPrice=avo_data)

        avo_data = json.dumps(db.get_price_range(date,location,avo_type))
        print(db.get_all_volume("Houston","organic"))
        #avo_vol = json.dumps(db.get_all_volume(location,avo_type))
        #print("HELLO???")
        #print(avo_data)

        return render_template('home.html', avoPrice = avo_data, loc = location, avo_type = avo_type)
    return redirect(url_for('login'))

@app.route("/register", methods = ['GET', 'POST'])
def create():
    
    # Get request method means go do the form
    if request.method == 'GET':
        return render_template('createAcc.html')

    # POST request method means new acc form submitted
    # get form fields
    usr = request.form['username']
    pswd = request.form['password']

    # create usr acc
    db.add_user(usr, pswd)

    return render_template('loginAcc.html', error="")

@app.route("/login", methods = ['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template("loginAcc.html")

    usr = request.form['username']
    pswd = request.form['password']

    if request.method == 'POST':
        if db.check_pass(usr, pswd):
            session["username"] = usr
            return redirect(url_for('index'))
        else:
            return render_template("loginAcc.html", error="Incorrect username or password")

@app.route("/log-out", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return render_template("error.html")

@app.route("/higher-Lower", methods = ['GET', 'POST'])
def game():
    if request.method == 'GET':
        
        date = db.get_random_date()
        start_date = db.get_start_date(date)
    
        invalid = True
        while invalid:
            stock = symbol_list[random.randint(0, len(symbol_list)-1)]
            stockTicker = stock['symbol']
            #print(stockName)
            if os.path.exists(f'./app/static/logos/{stockTicker}.png'):
                logo = f'./static/logos/{stockTicker}.png'
                stockName = stock['longName']
                stock_download = yf.download(stockTicker, start=start_date, end=date, interval='1wk', prepost=False)
                if stock_download.empty == False:
                    invalid = False
        
        while 1:
            if date.split("-")[0] == "2015" and (int(date.split("-")[1]) < 7):
                date = db.get_random_date()
            else:
                break
        print(date)

        location = db.get_random_location()
        if random.randint(0,1) == 0:
            avo_type = "organic"
        else:
            avo_type = "conventional"
        avo_data = json.dumps(db.get_price_range(date,location,avo_type))

        beginning_date = start_date
        stock_download = json.loads(yf.download(stockTicker, start=start_date, end=date, interval='1wk', prepost=False).to_json(orient='records'))
        #print(stock_download)
        compare_price = stock_download[0]['Close']
        stock_prices = {}
        for day in stock_download:
            if(start_date == "2020-11-29"):
                stock_prices[start_date] = day['Close'] / compare_price
                break
            stock_prices[start_date] = day['Close'] / compare_price
            start_date = db.get_next_date(start_date)
        stock_prices = json.dumps(stock_prices)
        #print(stock_prices)
        return render_template("higherLower.html", stock=stockName,logo=logo,avocado_data=avo_data,stock_data=stock_prices,start_date=beginning_date, end_date=date, location=location, avocado_type=avo_type)

@app.route("/leaderboard", methods = ['GET'])
def board():
    data = db.get_leaderboard()
    return render_template("leaderboard.html", data=data)

@app.route("/search", methods = ['GET'])
def search():
    return render_template("search.html")

@app.route("/you-lost", methods = ['GET'])
def lost():
    #get score from querystring
    score = request.args.get('score')
    #update db


    return render_template("lost.html", score=score)

if __name__ == "__main__":
    app.debug = True
    app.run()