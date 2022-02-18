# Projet_Flask_API
## Groupe 7 : Anouar, Eric, Arthur

Voici le résultat de notre projet API-REST pour le groupe 7  

### Backend  
J'ai utilisé me module Pyson pour créer un backend facile à mettre en oeuvre.  
Essentiellement la base de données est située dans le fichier flask_api_db.json.  
La base de données a été créée en ligne de commande avec l'instruction pysondb create flask_api_db.json.  
Le schéma de la base de données est fixée par sa première entrée.  
Comme le nom Pyson le suggère, les entrées se font au format JSON.

Pour plus de détails une descriptio du projet se trouve sur :  
https://dev.to/fredysomy/pysondb-a-json-based-lightweight-database-for-python-ija  

### Démarrage  
Dans le repo il faut lancer le fichier de l'app ./Flask_API/app_main.py  

### Route /create  
Dans cette route on passe une url via le paramètre url d'une requete get.  
Par exemple : 

### Route /read 


### Route /delete  



### Perspectives  
Dans une optique d'amélioration nous avont développer une 2nde version du projet qui nécessite SQLite3 pour fonctionner.  
Cette version utilise Bootstrap pour afficher Front-End au projet.  
Pour la lancer il faut activer le ./Flask_API_Bootstrap/main.py  
