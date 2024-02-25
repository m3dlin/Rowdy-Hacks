from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol


app = Flask(__name__,static_url_path='/static', static_folder='./static')

def find_barcode():
    print("IM working")
    

# first route when user goes to website.
@app.route("/")
def index():
    return render_template('scanner.html'), 200

@app.route('/upload', methods=['POST'])
def upload():
    # Get the image data URL from the request
    image_data_url = request.json['imageDataURL']
    
    # Process the image data URL as needed (e.g., save it to a file, analyze it, etc.)
    # Example: Save the image to a file
    with open('captured_photo.jpg', 'wb') as f:
       # f.write(image_data_url.split(',')[1].decode('base64'))
        f.write(base64.b64decode(image_data_url.split(',')[1]))

    find_barcode()
    return jsonify({'message': 'Image uploaded successfully' + extraStr})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)