import pymongo

def insert_nearbyroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    # 连接数据库
    db = client.spring
    # 选择dida这个数据库
    nearbyroute_collection = db.nearby
    # 选择集合，不存在的话自动创建（对应mysql的表概念）
    nearbyroute_collection.update({'id':info['id']}, info, True)
    # 插入数据，我这里用的是更新语句，意思是如果id已经存在的话，就不执行该条数据的插入动作，可以有效去重
    client.close()

def insert_cityroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.spring
    cityroute_collection = db.cityroute
    cityroute_collection.update({'id': info['id']}, info, True)
    client.close()

def insert_workroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.spring
    workroute_collection = db.workroute
    workroute_collection.update({'id': info['id']}, info, True)
    client.close()

def update_uesrinfo(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.spring
    userinfo_collection = db.userinfo
    userinfo_collection.update({'cid': info['cid']}, {"$set": {"cid":info['cid'], "gender": info['gender'], "name": info['name']}}, True)
    client.close()

def create_uesr(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.spring
    userinfo_collection = db.userinfo
    userinfo_collection.update({'cid': info['cid']}, info, True)
    client.close()
