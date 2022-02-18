# Projet_Flask_API
## Groupe 7 : Anouar, Eric, Arthur

Voici le résultat de notre projet API-REST pour le groupe 7  

### Backend  
Nous avons utilisé le module Pyson pour créer un backend facile à mettre en oeuvre.  
Essentiellement, la base de données est située dans le fichier flask_api_db.json.  
La base de données a été créée en ligne de commande avec l'instruction pysondb create flask_api_db.json.  
Le schéma de la base de données est fixée par sa première entrée.  
Comme le nom Pyson le suggère, les entrées se font au format JSON.  

Pyson ajoute un identifiant "id" de 18 chiffres à chaque entrée.  
C'est cet identifiant un peu complexe que nous utiliserons pour la plupart des opérations avec l'API.  

Pour plus de détails une description du projet Pyson se trouve sur :  
https://dev.to/fredysomy/pysondb-a-json-based-lightweight-database-for-python-ija  

### Démarrage  
Dans le repo il faut lancer le fichier de l'app ./Flask_API/app_main.py  
On verra en http://127.0.0.1:5000/ sur le navigateur le commentaire "API active".  

### Route /create  
Dans cette route on passe une url via le paramètre url d'une requete get.  
Si la requête fonctionne, on récupère l'identifiant du nouvel objet ainsi crée.  
En backend, la liste des mots parsés avec leur décompté est stockée et accessible via l'identifiant.  
Par exemple : http://127.0.0.1:5000/create?url=https://www.monde-diplomatique.fr/2022/02/TEURTRIE/64373

### Route /read  
L'identifiant est entré en aval de cette route après le signe "/".
Si la requête fonctionne, on récupère la liste des mots parsés avec leur décompte.  
Par exemple : http://127.0.0.1:5000/read/794533705597869327  

### Route /delete  
L'identifiant est entré en aval de cette route après le signe "/".
Par exemple : http://127.0.0.1:5000/delete/342076571809416181  

### Perspectives  
Dans une optique d'amélioration nous avont développer une 2nde version du projet qui nécessite SQLite3 pour fonctionner.  
Cette version utilise Bootstrap pour afficher Front-End au projet.  
Pour la lancer il faut activer le ./Flask_API_Bootstrap/main.py  
