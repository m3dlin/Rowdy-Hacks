from flask import Flask, render_template, request, redirect, url_for, session
from utils.database import check_credentials, get_dinosaurs_ids, get_dinosaurs_info, get_dinosaur_info
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
    return render_template('home.html'), 200


@app.route("/dinopedia")
def dinopedia_screen():
    return render_template('dinopedia.html'), 200


@app.route("/scan")
def scan_screen():
    return "<h1> scan screen </h1>"


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

@app.route("/<dino_name>")
def course_page(dino_name):
        if 'user' in session:
            user = session['user']
            dinosaur_info = get_dinosaur_info(dino_name)
            dinosaur_image = dinosaur_info[1]

            
            base64_image = base64.b64encode(dinosaur_info[1]).decode('utf-8')
            dino = {'name': dinosaur_image, 'image': base64_image}

            return render_template('dino-entry.html', dinosaur=dino), 200

@app.route("/capture")
def  dino_capture_screen():
    return render_template('dino-capture.html', status=True), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)