import pymongo
import pandas as pd
from pandas import Series,DataFrame

client = pymongo.MongoClient('127.0.0.1', 27017)
# 连接数据库
db = client['dida']
# 选择dida这个数据库
route = db['nearby']
from_info = route['from_poi']

df = DataFrame(list(route.find({"from_poi":{}})))
# del df['_id'],df['award_money'],df['city_id'],df['distance']


# df_from = DataFrame(list(from_info.find()), index=['street'])
print(df)
client.close()