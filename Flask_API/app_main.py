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
    return ("API active")

@app.route('/create', methods=['GET'])
def create():
    url = request.args.get('url')
    # creation liste de tuples mots : décompte (placeholder actuellement)
    vocabulary= {'crise': 0, 'des': 8, 'du': 4, 'en': 9, 'et': 6,  'la': 11, 'le': 5, 'les': 8, 'pour': 5,  'pourquoi': 1, 'se': 3, 'ukraine': 0, 'à': 8}
    newid = apidb.add({"name": url,"type":"entry", "words":vocabulary})
    return str(newid)

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