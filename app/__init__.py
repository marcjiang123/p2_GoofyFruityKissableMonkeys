# make this neater later
from flask import Flask, render_template, request, session, url_for, redirect
import db


app = Flask(__name__)
app.secret_key = "hjakdskajsdflkasjdflid"

@app.route("/")
@app.route("/home")
def index():
    if 'username' in session:
        return render_template('home.html')
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

    return render_template('loginAcc.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template("loginAcc.html")

    usr = request.form['username']
    pswd = request.form['password']

    if db.check_pass(usr, pswd):
        session["username"] = usr
        return redirect(url_for('index'))

@app.route("/log-out", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return render_template("error.html")

@app.route("/higher-Lower", methods = ['GET', 'POST'])
def game():
    return render_template("higherLower.html")

if __name__ == "__main__":
    app.debug = True
    app.run()