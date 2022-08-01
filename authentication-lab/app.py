from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

  "apiKey": "AIzaSyCPdzrQZU9L8rVRGAswqs3GnsQKB7CwgGE",

  "authDomain": "authenticationlab-98a5c.firebaseapp.com",

  "projectId": "authenticationlab-98a5c",

  "storageBucket": "authenticationlab-98a5c.appspot.com",

  "messagingSenderId": "959067420220",

  "appId": "1:959067420220:web:eea419df7f65a5dc65f539",

  "measurementId": "G-R5M1VD22GR",

  "databaseURL":""
}
  

firebase= pyrebase.initialize_app(config) 
auth=firebase.auth()
#db=firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
            return render_template("signin.html")
    return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
            return render_template("signup.html")
    return render_template ("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)