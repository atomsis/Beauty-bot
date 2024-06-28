from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mycollection']

# Добавление документа с меткой времени
document = {
    "name": "example_document",
    "createdAt": datetime.utcnow()
}
collection.insert_one(document)

# Создание TTL индекса
# 86400 = 24 часа 😁
collection.create_index("createdAt", expireAfterSeconds=86400)

print("Документ добавлен и TTL индекс создан.")
