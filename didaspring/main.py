from pyecharts import Pie,Bar,Line,GeoLines, Style
from pymongo import MongoClient
import json

global style,geo_style
# 定义图表初始化配置
style = Style(
    title_color="#fff",
    title_pos="center",
    width=1260,
    height=640,
    background_color="#08192D"
)
# geo风格配置
geo_style = style.add(
    legend_orient="vertical",
    legend_pos="left",
    legend_top = "center",
    legend_text_color="#fff",
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    geo_effect_symbol="plane",
    geo_effect_symbolsize=8,
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    symbol_size = 0.2,
    label_text_size=8,
    label_color=['#24936E','#6A4C9C','#0089A7','#BEC23F','#D0104C']

)
# 饼图风格配置
pie_style = style.add(
    legend_orient="vertical",
    legend_pos="left",
    legend_text_color="#fff",
    is_label_show=True,
    legend_top = "center",
    label_text_size=20,
)
# 柱状图风格配置
bar_style = style.add(
    legend_orient="vertical",
    legend_pos="left",
    legend_text_color="#fff",
    is_label_show=True,
    label_text_size=20,
    legend_top = "center",
    is_stack=True,
    xaxis_label_textsize=24,
    xaxis_label_textcolor="#fff",
    yaxis_label_textcolor = "#fff"
)
# 折线图风格配置
line_style = style.add(
    legend_orient="vertical",
    legend_pos="left",
    legend_text_color="#fff",
    is_label_show=True,
    legend_top = "center",
    label_text_size=24,
    is_stack=True,
    xaxis_label_textcolor="#fff",
    xaxis_label_textsize= 24,
    yaxis_label_textcolor = "#fff",
    label_color=['#24936E','#D0104C']
)

class SpringData:
    SpringData = []

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.spring = self.client.spring

    # 性别分析
    def getGender(self):
        collection = self.spring['cityroute']
        totalUser = collection.aggregate([{
            '$group':{
                '_id':'$passenger_user_info.gender',
                'Gnum':{
                    '$sum': 1
                }
            }
        }])
        attr = ["男乘客","女乘客","性别不详"]
        listnum = list(totalUser)
        male = listnum[0]['Gnum']
        female = listnum[2]['Gnum']
        nomale = listnum[1]['Gnum']
        value = [male,female,nomale]
        genderpie = Pie("性别比例",**style.init_style)
        genderpie.add("性别",attr,value, **pie_style)
        genderpie.render("results/gender.html")
        print(male,female,nomale)

    # 订单数分析
    def getCityAll(self):
        collection = self.spring['cityroute']
        result_hangzhou = collection.aggregate([
            {'$match':{'from_poi.city.city_name':'杭州'}},
            {'$group':{'_id':'$passenger_user_info.gender','count':{'$sum':1}}}
        ])
        result_beijing = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '北京'}},
            {'$group': {'_id': '$passenger_user_info.gender', 'count': {'$sum': 1}}}
        ])
        result_shanghai = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '上海'}},
            {'$group': {'_id': '$passenger_user_info.gender', 'count': {'$sum': 1}}}
        ])
        result_guangzhou = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '广州'}},
            {'$group': {'_id': '$passenger_user_info.gender', 'count': {'$sum': 1}}}
        ])
        result_shenzhen = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '深圳'}},
            {'$group': {'_id': '$passenger_user_info.gender', 'count': {'$sum': 1}}}
        ])
        result_hangzhou_ = list(result_hangzhou)
        result_hangzhou_male = result_hangzhou_[0]["count"]
        result_hangzhou_female = result_hangzhou_[2]["count"]
        result_hangzhou_nomale = result_hangzhou_[1]["count"]
        result_beijing_ = list(result_beijing)
        result_beijing_male = result_beijing_[0]["count"]
        result_beijing_female = result_beijing_[2]["count"]
        result_beijing_nomale = result_beijing_[1]["count"]
        result_shanghai_ = list(result_shanghai)
        result_shanghai_male = result_shanghai_[0]["count"]
        result_shanghai_female = result_shanghai_[2]["count"]
        result_shanghai_nomale = result_shanghai_[1]["count"]
        result_guangzhou_ = list(result_guangzhou)
        result_guangzhou_male = result_guangzhou_[0]["count"]
        result_guangzhou_female = result_guangzhou_[2]["count"]
        result_guangzhou_nomale = result_guangzhou_[1]["count"]
        result_shenzhen_ = list(result_shenzhen)
        result_shenzhen_male = result_shenzhen_[0]["count"]
        result_shenzhen_female = result_shenzhen_[2]["count"]
        result_shenzhen_nomale = result_shenzhen_[1]["count"]
        citybar = Bar("各城市订单情况",page_title = "各城市订单情况",**style.init_style)
        attr = ["北京","上海","广州","深圳","杭州"]
        male_value = [result_beijing_male,result_shanghai_male,result_guangzhou_male,result_shenzhen_male,result_hangzhou_male]
        female_value = [result_beijing_female,result_shanghai_female,result_guangzhou_female,result_shenzhen_female,result_hangzhou_female]
        nomale_value = [result_beijing_nomale,result_shanghai_nomale,result_guangzhou_nomale,result_shenzhen_nomale,result_hangzhou_nomale]
        citybar.add("男乘客",attr,male_value,**bar_style)
        citybar.add("女乘客", attr, female_value,**bar_style)
        citybar.add("性别不详", attr, nomale_value,**bar_style)
        citybar.render("results/city.html")

    # 路线图分析
    def getLines(self):
        collection = self.spring['cityroute']
        line_hangzhou = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '杭州'}},
            {'$group': {'_id': '$to_poi.city.city_name', 'count': {'$sum': 1}}}
        ])
        line_beijing = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '北京'}},
            {'$group': {'_id': '$to_poi.city.city_name', 'count': {'$sum': 1}}}
        ])
        line_shanghai = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '上海'}},
            {'$group': {'_id': '$to_poi.city.city_name', 'count': {'$sum': 1}}}
        ])
        line_guangzhou = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '广州'}},
            {'$group': {'_id': '$to_poi.city.city_name', 'count': {'$sum': 1}}}
        ])
        line_shenzhen = collection.aggregate([
            {'$match': {'from_poi.city.city_name': '深圳'}},
            {'$group': {'_id': '$to_poi.city.city_name', 'count': {'$sum': 1}}}
        ])
        line_hangzhou_ = []
        for line in line_hangzhou:
            line_hangzhou_.append(["杭州",line['_id'],line['count']])
        line_beijing_ = []
        for line in line_beijing:
            line_beijing_.append(["北京", line['_id'], line['count']])
        line_shanghai_ = []
        for line in line_shanghai:
            line_shanghai_.append(["上海", line['_id'], line['count']])
        line_guangzhou_ = []
        for line in line_guangzhou:
            line_guangzhou_.append(["广州", line['_id'], line['count']])
        line_shenzhen_ = []
        for line in line_shenzhen:
            line_shenzhen_.append(["深圳", line['_id'], line['count']])

        citylines = GeoLines("春节迁移路线图", **style.init_style)
        citylines.add("从北京出发",
                      line_beijing_,
                      **geo_style)
        citylines.add("从上海出发",
                      line_shanghai_,
                      **geo_style)
        citylines.add("从广州出发",
                      line_guangzhou_,
                      **geo_style)
        citylines.add("从深圳出发",
                      line_shenzhen_,
                      **geo_style)
        citylines.add("从杭州出发",
                      line_hangzhou_,
                      **geo_style)
        citylines.render("results/citylines.html")

    # 客单价分析
    def getAvgPrice(self):
        collection = self.spring['cityroute']
        avg_price = collection.aggregate([
            {'$group':{'_id':'$from_poi.city.city_name','avg_price':{'$avg':'$price'}}}
            ])
        city_avg_price = list(avg_price)
        city_avg_price = sorted(city_avg_price, key=lambda city:city['avg_price'])
        pricebar = Bar("各城市顺风车平均单价",page_title="各城市顺风车平均单价",**style.init_style)
        attr = [city_avg_price[0]['_id'],city_avg_price[1]['_id'],city_avg_price[2]['_id'],city_avg_price[3]['_id'],city_avg_price[8]['_id']]
        value = ['%.2f'%(city_avg_price[0]['avg_price']),'%.2f'%(city_avg_price[1]['avg_price']),'%.2f'%(city_avg_price[2]['avg_price']),'%.2f'%(city_avg_price[3]['avg_price']),'%.2f'%(city_avg_price[8]['avg_price'])]
        pricebar.add("城市",attr,value,**bar_style)
        pricebar.render("results/avgpricebar.html")
        print(city_avg_price)

    # 加价分析
    def getThanks(self):
        collection = self.spring['cityroute']
        count_thanks = collection.aggregate([
            {'$match':{'thanks_price':{'$gt':0}}},
            {'$group':{'_id':'$from_poi.city.city_name','avg_thanks_price':{'$avg':'$thanks_price'},'count_thanks':{'$sum':1}}}
        ])
        thanks_result = list(count_thanks)
        thanks_result = sorted(thanks_result,key=lambda city: city['avg_thanks_price'])
        print(thanks_result)
        thanksline = Line("哪里的乘客最壕气",page_title="哪里的乘客最壕气",**style.init_style)
        count_value = ['%.2f'%(thanks_result[3]['count_thanks']/11.74),'%.2f'%(thanks_result[4]['count_thanks']/46.34),'%.2f'%(thanks_result[6]['count_thanks']/17.32),'%.2f'%(thanks_result[7]['count_thanks']/27.15),'%.2f'%(thanks_result[8]['count_thanks']/20.83)]
        avg_value = ['%.2f'%(thanks_result[3]['avg_thanks_price']),'%.2f'%(thanks_result[4]['avg_thanks_price']),'%.2f'%(thanks_result[6]['avg_thanks_price']),'%.2f'%(thanks_result[7]['avg_thanks_price']),'%.2f'%(thanks_result[8]['avg_thanks_price'])]
        attr = [thanks_result[3]['_id'], thanks_result[4]['_id'], thanks_result[6]['_id'], thanks_result[7]['_id'],
                thanks_result[8]['_id']]
        thanksline.add("比例",attr,count_value,**line_style)
        thanksline.add("平均加价",attr,avg_value,**line_style)
        thanksline.render("results/thanksline.html")


    # 导出Kepler地图格式的json文件
    def getKepler(self):
        collection = self.spring['cityroute']
        results = list(collection.find({},{"_id":0,"from_poi.longitude":1,"from_poi.latitude":1,"to_poi.longitude":1,"to_poi.latitude":1,}))
        kepler_data = []
        for result in results:
            kepler_data.append({
                "from_lng":result['from_poi']['longitude'],
                "from_lat":result['from_poi']['latitude'],
                "to_lng":result['to_poi']['longitude'],
                "to_lat":result['to_poi']['latitude']
            })
        kepler_json = json.dumps(kepler_data)
        file = open('results/kepler.json','w')
        file.write(kepler_json)
        file.close()
        pass


test = SpringData()
test.getKepler()