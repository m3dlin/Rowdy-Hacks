from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from utils.database import check_credentials, get_dinosaurs_ids, get_dinosaurs_info, get_dinosaur_info, get_dinosaur
import base64
import os
from dotenv import load_dotenv
import random
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

# Define probabilities for each number
probabilities = {
    1: 0.6,  # 60% chance
    2: 0.25,  # 25% chance
    3: 0.1,   # 10% chance
    4: 0.05   # 5% chance
}


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
    return render_template('scanner.html'), 200


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




@app.route('/upload_code', methods=['POST', 'GET'])
def upload_code():
    if request.method == 'POST':
    # Get the image data URL from the request
        code = request.json['code']

    # 4101450004474
    # # print(code.encode('utf-8'))
    # # Save the barcode data to a file
    # with open('barcode_txt', 'wb') as f:
    #    # f.write(image_data_url.split(',')[1].decode('base64'))
    #     # f.write(code)
    #     f.write(code.encode('utf-8'))

    # find_barcode()
        return redirect(url_for('capture')), 302
    # return jsonify({'message': 'Code uploaded successfully'})

@app.route("/capture", endpoint='capture')
def  dino_capture_screen():
    # Generate a random number based on probabilities
    dinoID = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
    

    dinosaur_info = get_dinosaur(dinoID)
    dinosaur_image = dinosaur_info[1]

            
    base64_image = base64.b64encode(dinosaur_info[1]).decode('utf-8')
    dino = {'name': dinosaur_image, 'image': base64_image}
    return render_template('dino-capture.html', dinosaur=dino), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)