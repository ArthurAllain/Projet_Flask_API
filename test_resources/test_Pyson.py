from pysondb import db

apidb=db.getDb('flask_api_db.json')

#apidb.add({"name":"py_cli","type":"CLI"})

# The data wont be added as the key "name" is mispelled as "namme"
# apidb.add({"namme":"pyson","type":"DB"})

#print(apidb.get(1))

print(apidb.getBy({"type":"CLI"}))