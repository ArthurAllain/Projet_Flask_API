from logging import root
from flask import Flask
from flask import request
from pysondb import db

# creation de l'application
app = Flask(__name__)

# connection de la DB Pyson
apidb=db.getDb('flask_api_db.json')

@app.route('/')
def home():
    return ("app en fonction")

@app.route('/create')
def create():
    url = request.args.get('url')
    return url

@app.route('/read')
def read():
    return

@app.route('/update')
def update():
    return

@app.route('/delete')
def delete():
    return

@app.route('/graph')
def graph():
    return

@app.route('/flush')
def flush():
    return

#run the application
if __name__ == "__main__":
    app.run(debug=True)