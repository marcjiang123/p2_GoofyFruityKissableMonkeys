# make this neater later
from flask import Flask, render_template, request, session, url_for, redirect
from stocksymbol import StockSymbol
import db
import random
import requests
import os
import populate

app = Flask(__name__)
app.secret_key = "hjakdskajsdflkasjdflid"

ss = StockSymbol('9625612b-526c-4289-af96-076826ab74a2')
symbol_list = ss.get_symbol_list(index='SPX')

@app.route("/")
@app.route("/home")
def index():
    if 'username' in session:
        return render_template('home.html', testparam= "new Date(2021, 3, 1)")
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
        valid = False
        while not valid:
            stock = symbol_list[random.randint(0, len(symbol_list)-1)]
            stockTicker = stock['symbol']
            #print(stockName)
            if os.path.exists(f'./app/static/logos/{stockTicker}.png'):
                logo = f'./static/logos/{stockTicker}.png'
                stockName = stock['longName']
                valid = True
        
        date = db.get_random_date()
        print(date)
        return render_template("higherLower.html", stock=stockName,logo=logo)

@app.route("/leaderboard", methods = ['GET'])
def board():
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.debug = True
    app.run()