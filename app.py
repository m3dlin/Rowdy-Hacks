from flask import Flask, render_template, request, redirect, url_for, session
from utils.database import check_credentials, get_dinosaurs_ids, get_dinosaurs_info
import base64
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')


# first route when user goes to website.
@app.route("/")
def index():
    return render_template('login-screen.html'), 200

@app.route("/login", methods=['POST'], endpoint='login')
def login():
    if request.method == 'POST':
        email = request.form['email']

        # sends the form answers to be verified. If successful, redirect user to the home page
        if check_credentials(email=email):
            session['user'] = request.form['email']
            return redirect(url_for('home'))
    return redirect("/")
    
@app.route("/home", endpoint='home')
def home_screen():
    return "<h1> hello world </h1>"

@app.route("/inventory")
def inventory_screen():
    if 'user' in session:
        user = session['user']
        dinosaur_ids = get_dinosaurs_ids(user)
        dinosaur_data = get_dinosaurs_info(dinosaur_ids)
        
        # Convert binary image data to Base64-encoded strings
        dinosaurs = []
        for dinosaur_name, dinosaur_image in dinosaur_data:
            base64_image = base64.b64encode(dinosaur_image).decode('utf-8')
            dinosaurs.append({'name': dinosaur_name, 'image': base64_image})

        return render_template('inventory.html', dinosaurs=dinosaurs), 200




    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)