from pymongo import MongoClient
# pymongo를 쓰겠슴둥
client = MongoClient('localhost', 27017)
# 내 컴터에 지금 돌아가고 있는 mongoDB에 접속할 거임
db = client.dbsparta
# dbsparta 라고 하는 DB 이름으로 접속할 겁니다. (없으면 자동으로 만들어짐)

# insert / find / update / delete
# 코딩 시작
# ---------- insert -----------------
# doc = {'name':'jane','age':21}
# db.users.insert_one(doc)


# ---------- find -----------------

# same_ages = list(db.users.find({'age':21},{'_id':False}))
# # same_ages = list(db.users.find({},{'_id':False}))    조건이 없을 땐 빈 중괄호하면 됨~
# for person in same_ages:
#     print(person)

# ---------- find_one -----------------
# # 젤 위에 있는 것들만 찾아와욥~
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)

# ---------- update_one -----------------
# # 젤 위에 있는 것들만 바꿔욥~
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# ---------- update_many -----------------
# # name이 bobby인 애들을 모두 찾아서 age를 19로 바꿔줘욥~ 하지만 위험해서 잘 쓰진 않아욥~
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# ---------- delete_one -----------------
# db.users.delete_one({'name':'bobby'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})