from pymongo import MongoClient
# pymongo를 쓰겠슴둥
client = MongoClient('localhost', 27017)
# 내 컴터에 지금 돌아가고 있는 mongoDB에 접속할 거임
db = client.dbsparta
# dbsparta 라고 하는 DB 이름으로 접속할 겁니다. (없으면 자동으로 만들어짐)

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']
movies = list(db.movies.find({'star':target_star}))
for movie in movies:
    print(movie['title'])