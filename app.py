from flask import Flask, render_template

app = Flask(__name__)



dinosaurs_data = {
  "buddy 1",
  "buddy 2",
  "rowdy-rex",
  "datasaur",
}


# first route when user goes to website.
@app.route("/")
def index():
    return render_template('inventory.html', dinosaurs = dinosaurs_data), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)