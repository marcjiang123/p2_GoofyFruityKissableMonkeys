from flask import Flask, render_template, request, session



app = Flask(__name__)
totallySecure = {} #This is temporary until DB for passwords

@app.route("/")
@app.route("/index")
def index():
    if 'username' in session:
        return render_template('home.html')
    return render_template('loginAcc.html')

@app.route("/register", methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        return render_template('loginAcc.html')

    return render_template('createAcc.html')



if __name__ == "__main__":
    app.debug = True
    app.run()