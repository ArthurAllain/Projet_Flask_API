from logging import root
from flask import Flask


# creation de l'application
app = Flask(__name__)

@app.route('/')
def home():
    return ("Hello World!")

#run the application
if __name__ == "__main__":
    app.run(debug=True)