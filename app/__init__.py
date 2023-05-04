from flask import Flask, render_template, request, session



app = Flask(__name__)
totallySecure = {} #This is temporary until DB for passwords

@app.route("/")
@app.route("/index")
def index():
    if 'username' in session:
        return render_template('home.html')
    return render_template('loginAcc.html')

@app.route("/register")
def create():
    if request.method == "GET":
        return render_template('createAcc.html')

    return render_template('loginAcc.html')



if __name__ == "__main__":
    app.debug = True
    app.run()