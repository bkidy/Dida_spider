import pymongo

def insert_nearbyroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    # 连接数据库
    db = client.dida
    # 选择dida这个数据库
    nearbyroute_collection = db.nearby
    # 选择集合，不存在的话自动创建（对应mysql的表概念）
    nearbyroute_collection.update({'id':info['id']}, info, True)
    # 插入数据，我这里用的是更新语句，意思是如果id已经存在的话，就不执行该条数据的插入动作，可以有效去重
    client.close()

def insert_cityroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.dida
    cityroute_collection = db.cityroute
    cityroute_collection.update({'id': info['id']}, info, True)
    client.close()

def insert_workroute(info):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.dida
    workroute_collection = db.workroute
    workroute_collection.update({'id': info['id']}, info, True)
    client.close()
