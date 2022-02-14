from logging import root
from flask import Flask


# creation de l'application
app = Flask(__name__)

@app.route('/')
def home():
    return ("Hello World!")

#run the application
app.run(debug=True)