from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://camilohamon:HuLlschb0Kl3vQ6v@cluster0.mk5svw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient("mongodb+srv://camilohamon:HuLlschb0Kl3vQ6v@cluster0.mk5svw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection = db.todo_collection

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)




