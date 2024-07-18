import pymongo

# DOCKER CONFIG
# MONGO_HOST='mongo-server'
# LOCAL CONFIG
MONGO_HOST='localhost'
MONGO_PORT='27017'
MONGO_TIMEOUT=1000
MONGO_URI='mongodb://'+MONGO_HOST+':'+MONGO_PORT

client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIMEOUT)
client.server_info()
db = client.duties
collection = db.duties_collection

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)