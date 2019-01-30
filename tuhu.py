import ssl
import requests
import json
import pymongo
import urllib.parse
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

brandUrl = 'https://api.tuhu.cn/Vehicle/SelectVehicleAllBrands'
vehicleUrl = 'https://api.tuhu.cn/Vehicle/SelectVehicleInfoByBrand'
carUrl = 'https://api.tuhu.cn/Vehicle/SelectVehicle'


brandResponse = requests.get(brandUrl)
if brandResponse:
    brands = json.loads(brandResponse.text).get('Brand')
    for brand in brands:
        brandName = brand.get('Brand')
        brandLogoUrl = brand.get('ImageUrl')
        # 获取品牌名称
        print(brandName)
        vehicleResponse = requests.get(vehicleUrl, data={'brand': brandName})
        if vehicleResponse:
            # 将品牌名称作为参数，获取车系
            vehicles = json.loads(vehicleResponse.text).get('OneBrand')
            for vehicle in vehicles:
                brandType = vehicle.get('BrandType')
                carSeries = vehicle.get('CarName')
                seriesImage = vehicle.get('Image')
                vehicleName = vehicle.get('Vehicle')
                vehicleId = vehicle.get('ProductID')
                seriesImageSmall = vehicle.get('Src')
                tires = vehicle.get('Tires')
                # 获取车系ID
                print(vehicleName)
                plResponse = requests.get(carUrl, data={'vehicleId': vehicleId})
                if plResponse:
                    pls = json.loads(plResponse.text).get('PaiLiang')
                    for pl in pls:
                        print(pl)
                        nianResponse = requests.get(carUrl, data={'vehicleId':vehicleId,'pailiang': pl})
                        if nianResponse:
                            nians = json.loads(nianResponse.text).get('Nian')
                            for nian in nians:
                                print(nian)
                                carResponse = requests.get(carUrl, data={'vehicleId': vehicleId, 'pailiang': pl, 'nian': nian})
                                if carResponse:
                                    cars = json.loads(carResponse.text).get('SalesName')
                                    for car in cars:
                                        carInfo = {
                                            "Tid": car['Tid'],
                                            "SalesName": car['SalesName'],
                                            "AvgPrice": car['AvgPrice'],
                                            "BrandName": brandName,
                                            "BrandLogo": brandLogoUrl,
                                            "BrandType": brandType,
                                            "CarSeries": carSeries,
                                            "SeriesImage": seriesImage,
                                            "SeriesID": vehicleId,
                                            "SeriesImage-small": seriesImageSmall,
                                            "Tires": tires,
                                            "Year": nian,
                                            "Displacement": pl,
                                        }
                                        client = pymongo.MongoClient('127.0.0.1', 27017)
                                        # 连接数据库
                                        db = client.dida
                                        # 选择dida这个数据库
                                        cars_collection = db.cars
                                        # 选择集合，不存在的话自动创建（对应mysql的表概念）
                                        cars_collection.update({'Tid': carInfo['Tid']}, carInfo, True)
                                        # 插入数据，我这里用的是更新语句，意思是如果id已经存在的话，就不执行该条数据的插入动作，可以有效去重
                                        # client.close()
                                        print(carInfo)


