from cgitb import text
from ssl import AlertDescription
from unittest import result
from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3
import nltk
from newspaper import Article



app = Flask(__name__,template_folder='template')
"""     
# recuperation de la valeur du champ url du formulaire
url = request.form['url']

# traitement de l'url avec nltk
article = Article(url)
article.download()
article.parse()
article.text
article.nlp()
mots = article.keywords
# mettre les mots clés dans une liste avec leur fréquence
mots_freq = nltk.FreqDist(mots)
# trier les mots clés par fréquence et les mettre dans un tuple
wrds = mots_freq.most_common(10)

"""

# root de creation de bdd 
@app.route('/')
def home():
    conn = sqlite3.connect('api.db')
    cur = conn.cursor()
    req = "CREATE TABLE IF NOT EXISTS api (id INTEGER PRIMARY KEY, text TEXT)"
    cur.execute(req)
    conn.commit()
    conn.close()
    return render_template('home.html')

#route pour faire l'insertion dans la base de données du wrds
@app.route('/insert', methods=['POST'])
def insert():
    conn = sqlite3.connect('api.db')
    cur = conn.cursor()
    req = "INSERT INTO api (text) VALUES (?)"
    cur.execute(req, (text,))
    conn.commit()
    conn.close()
    #message de confirmation
    msg = "Insertion réussie"
    return render_template('home.html', msg=msg)
   

# route pour afficher le tuple dans le champ resultat
@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        conn = sqlite3.connect('api.db')
        cur = conn.cursor()
        req = "SELECT * FROM api"
        cur.execute(req)
        rows = cur.fetchall()
        conn.close()
        return rows
    return render_template('home.html', rows=rows)
    
   

   
#route pour faire la suppression dans la base de données
@app.route('/delete', methods=['GET', 'POST'])  
def delete_db(id):
    conn = sqlite3.connect('api.db')
    cur = conn.cursor()
    req = "DELETE FROM api WHERE id = ?"
    cur.execute(req, (id,))
    conn.commit()
    conn.close()
    #afficher une alerte pour dire que la suppression est faite
    msg = "Suppression faite"
    return render_template('home.html', msg=msg)

#route pour faire la modification dans la base de données
@app.route('/update', methods=['GET', 'POST'])
    #methode pour modifier le tuple de la base de données
def update_db(id, text):
    conn = sqlite3.connect('api.db')
    cur = conn.cursor()
    req = "UPDATE api SET text = ? WHERE id = ?"
    cur.execute(req, (text, id))
    conn.commit()
    conn.close() 
    #afficher une alerte pour dire que la modification est faite
    msg = "Modification faite"
    return render_template('home.html', msg=msg)
    

if __name__ == '__main__':
    app.run(debug=True)
    