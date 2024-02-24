from flask import Flask, render_template

app = Flask(__name__)

# first route when user goes to website.
@app.route("/")
def index():
    return render_template('index.html'), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)