# Dino Detectors🦖
Dino Detectors, the modern take on the classic Skannerz toy! Users can explore, scan and collect a diverse range of dinosaurs, bringing the thrill of discovery.

This project was the result of a group of four developers who attended RowdyHacks 2024. The languages and tools used to create Dino Detectors includes: HTML/CSS, Bootstrap, Python, Flask, JavaScript, Web APIs (MediaStream, GetUserMedia, QuaggaJS, and MediaDevicesAPI), MySQL Workbench, PlanetScale, and Render.

<img width="188" alt="Screenshot 2024-02-26 at 11 05 27 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/31fb8135-8636-4cf3-914b-b4bd7766960d"><img width="190" alt="Screenshot 2024-02-26 at 11 08 18 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/a43848ed-dae3-4978-bc77-3951ada942c6"><img width="190" alt="Screenshot 2024-02-26 at 11 07 23 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/56287437-d296-4def-99ef-83efd3dc0963"><img width="188" alt="Screenshot 2024-02-26 at 11 07 34 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/5b5adc20-8419-490b-aa5e-d10d1cd33c51"><img width="188" alt="Screenshot 2024-02-26 at 11 07 52 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/20850e58-fa11-49f3-ad29-af268e56b25e"><img width="188" alt="Screenshot 2024-02-26 at 11 08 06 AM" src="https://github.com/m3dlin/Rowdy-Hacks/assets/110800525/ef852849-9ca7-4155-b9f8-9bca6d8894c4">




## Installation🛠️

1. Open to the desired directory location.

2. Clone the repository using
```sh
git clone https://github.com/m3dlin/Rowdy-Hacks.git
```

3. Install all dependencies
```sh
pip install -r requirements.txt
```

## Usage📱🤳

Dino Detector is a web application with the purpose of being accessible to anyone with a smartphone. The app allows you to scan barcodes and, if you're lucky, a dinosaur will appear that you can capture. When you capture the dinosaur, you can view it in your inventory. The inventory showcases all the dinosaurs you have thus far. There is also a Dinopedia page to learn more about the dinosaurs and their traits.

The website is currently hosted on render at [https://rowdy-hacks.onrender.com](https://rowdy-hacks.onrender.com)


## Local Development
Run the app in development mode using
```sh
python app.py
```
open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in your browser


### Accessing User and Password Credentials
To access user and password credentials for the database connection in this project, follow these steps:

#### Prerequisites
- Ensure you have the necessary permissions and access rights to use the database.

#### Configuration File
IMPORTANT: To be able to work locally on a development server, you must add the database credentials into a .env file within root of project. Here's a template below -

Example `.env` structure:
```env
DATABASE_HOST=your_host
DATABASE_USERNAME=your_username
DATABASE_PASSWORD=your_password
DATABASE=your_database_name

SECRET_KEY=your_secret_key
```
