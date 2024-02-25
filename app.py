from flask import Flask, render_template, request, redirect, url_for, session
from utils.database import check_credentials
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

dinosaurs_data = {
  "buddy 1",
  "buddy 2",
  "rowdy-rex",
  "datasaur",
}


# first route when user goes to website.
@app.route("/")
def index():
    return render_template('login-screen.html'), 200

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        # sends the form answers to be verified. If successful, redirect user to the home page
        if check_credentials(email=email):
            session['email'] = request.form['email']
            return redirect(url_for('home'))
    return redirect("/")
    
@app.route("/home", endpoint='home')
def home_screen():
    return "<h1> hello world </h1>"

@app.route("/inventory")
def inventory_screen():
    return render_template('inventory.html', dinosaurs = dinosaurs_data), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)