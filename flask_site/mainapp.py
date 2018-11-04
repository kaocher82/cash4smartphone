
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/<string:button>")
def hello(button):
    button = button.capitalize()
    return f"<h1>hello {button}</h1>"
