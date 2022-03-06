from pymongo import MongoClient
# pymongo를 쓰겠슴둥
client = MongoClient('localhost', 27017)
# 내 컴터에 지금 돌아가고 있는 mongoDB에 접속할 거임
db = client.dbsparta
# dbsparta 라고 하는 DB 이름으로 접속할 겁니다. (없으면 자동으로 만들어짐)

db.movies.update_one({'title':'매트릭스'},{'$set': {'star': '0'}})