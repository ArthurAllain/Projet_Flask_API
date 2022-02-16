from logging import root
from flask import Flask
from flask import request
from pysondb import db

import nltk
from newspaper import Article
nltk.download('punkt')

from nltk.tokenize import word_tokenize

# creation de l'application
app = Flask(__name__)

# connection de la DB Pyson
apidb=db.getDb('flask_api_db.json')

@app.route('/')
def home():
    return ("API active")

@app.route('/create')
def create():
    # creation liste de tuples mots : décompte
    #vocabulary= {'crise': 0, 'des': 8, 'du': 4, 'en': 9, 'et': 6,  'la': 11, 'le': 5, 'les': 8, 'pour': 5,  'pourquoi': 1, 'se': 3, 'ukraine': 0, 'à': 8}
    url = request.args.get('url')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    wrd = word_tokenize(article.text)
    wrd_count = nltk.FreqDist(wrd)
    
    newid = apidb.add({"name": url,"type":"url_entry", "words": wrd_count })
    return str(newid)

@app.route('/read/<currentid>', methods=['GET'])
def read(currentid):
    res = apidb.getById(currentid)
    return str(res['words'])

@app.route('/update')
def update():
    return

@app.route('/delete/<currentid>')
def delete(currentid):
    res = apidb.deleteById(currentid)
    return str(currentid)

@app.route('/graph')
def graph():
    return

@app.route('/flush')
def flush():
    return

#run the application
if __name__ == "__main__":
    app.run(debug=True)