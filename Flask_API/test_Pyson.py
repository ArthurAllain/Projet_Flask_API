from pysondb import db

apidb=db.getDb('flask_api_db.json')

apidb.add({"name":"pysondb","type":"DB"})
apidb.add({"namme":"pyson","type":"DB"})
# The data wont be added as the key "name" is mispelled as "namme"