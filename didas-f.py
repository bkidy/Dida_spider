import json
from handle_db import insert_nearbyroute, insert_cityroute, insert_workroute
import time


def trsf_time(intime):
    # 时间格式转换的方法，下面转换时间用的
    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(intime, "%Y%m%d%H%M%S"))
    return new_time


def response(flow):
    nearbyroute_url1 = 'http://211.151.134.222/V3/BookingDriver/getNearbyBookingRideList'
    nearbyroute_url2 = 'http://211.151.12.10/V3/BookingDriver/getNearbyBookingRideList'
    cityroute_url1 = 'http://211.151.134.222/V3/BookingDriver/getRideListByRoute'
    cityroute_url2 = 'http://211.151.12.10/V3/BookingDriver/getRideListByRoute'
    workroute_url1 = 'http://211.151.134.222/V3/BookingDriver/getBookingRideList'
    workroute_url2 = 'http://211.151.12.10/V3/BookingDriver/getBookingRideList'
    # 我们需要抓取数据的几个接口URL，APP会不定时改变请求地址，所以每个接口有两个地址
    # DiyRoute = 'http://211.151.134.222/V3/BookingDriver/getBookingRideListV2'
    if nearbyroute_url1 in flow.request.url or nearbyroute_url2 in flow.request.url:
        text = flow.response.content
        # 将接口response内容赋值给text，这里需要注意 flow.response.text（已解码） 和 flow.response.content（二进制）的区别
        # 一开始用的是text，无奈中文乱码怎麽都搞不定，后来就用context试了一下，成功
        text = json.loads(text)
        # json.loads 将json格式数据转化成字典
        nearbyroutes = text.get('list')
        for nearbyroute in nearbyroutes:
            award_money = nearbyroute.get('award_money')
            city_id = nearbyroute.get('city_id')
            create_time = trsf_time(nearbyroute.get('create_time'))
            distance = nearbyroute.get('distance')
            driver_received_price = nearbyroute.get('driver_received_price')
            from_poi = nearbyroute.get('from_poi')
            f_business = from_poi.get('business')
            f_city = from_poi.get('city')
            f_city_name = f_city.get('city_name')
            f_provice_name = f_city.get('province_name')
            f_latitude = from_poi.get('latitude')
            f_longitude = from_poi.get('longitude')
            f_long_address = from_poi.get('long_address')
            f_short_address = from_poi.get('short_address')
            f_street = from_poi.get('street')
            id = nearbyroute.get('id')
            passenger_user_info = nearbyroute.get('passenger_user_info')
            cid = passenger_user_info.get('cid')
            gender = passenger_user_info.get('gender')
            name = passenger_user_info.get('name')
            plan_start_time = trsf_time(nearbyroute.get('plan_start_time'))
            price = nearbyroute.get('price')
            thanks_price = nearbyroute.get('thanks_price')
            time_scale_mins = nearbyroute.get('time_scale_mins')
            to_poi = nearbyroute.get('to_poi')
            t_business = to_poi.get('business')
            t_city = to_poi.get('city')
            t_city_name = t_city.get('city_name')
            t_provice_name = t_city.get('province_name')
            t_latitude = to_poi.get('latitude')
            t_longitude = to_poi.get('longitude')
            t_long_address = to_poi.get('long_address')
            t_short_address = to_poi.get('short_address')
            t_street = to_poi.get('street')
            nearbyroute_info = {
                'award_money': award_money,
                'city_id': city_id,
                'create_time': create_time,
                'distance': distance,
                'driver_received_price': driver_received_price,
                'from_poi': {
                    'business': f_business,
                    'city': {
                        'city_name': f_city_name,
                        'province_name': f_provice_name
                    },
                    'latitude': f_latitude,
                    'long_address': f_long_address,
                    'longitude': f_longitude,
                    'short_address': f_short_address,
                    'street': f_street
                },
                'id': id,
                'passenger_user_info': {
                    'cid': cid,
                    'gender': gender,
                    'name': name
                },
                'plan_start_time': plan_start_time,
                'price': price,
                'thanks_price': thanks_price,
                'time_scale_mins': time_scale_mins,
                'to_poi': {
                    'business': t_business,
                    'city': {
                        'city_name': t_city_name,
                        'province_name': t_provice_name
                    },
                    'latitude': t_latitude,
                    'long_address': t_long_address,
                    'longitude': t_longitude,
                    'short_address': t_short_address,
                    'street': t_street
                }
            }
            print(nearbyroute_info)
            insert_nearbyroute(nearbyroute_info)
            # 调用数据库插入方法插入数据

    if workroute_url1 in flow.request.url or workroute_url2 in flow.request.url:
        text = flow.response.content
        text = json.loads(text)
        WorkRoutes = text.get('list')
        for WorkRoute in WorkRoutes:
            create_time = trsf_time(WorkRoute.get('create_time'))
            distance = WorkRoute.get('distance')
            driver_received_price = WorkRoute.get('driver_received_price')
            from_poi = WorkRoute.get('from_poi')
            f_business = from_poi.get('business')
            f_city = from_poi.get('city')
            f_city_name = f_city.get('city_name')
            f_provice_name = f_city.get('province_name')
            f_latitude = from_poi.get('latitude')
            f_longitude = from_poi.get('longitude')
            f_long_address = from_poi.get('long_address')
            f_short_address = from_poi.get('short_address')
            f_street = from_poi.get('street')
            id = WorkRoute.get('id')
            passenger_user_info = WorkRoute.get('passenger_user_info')
            cid = passenger_user_info.get('cid')
            gender = passenger_user_info.get('gender')
            name = passenger_user_info.get('name')
            phone = passenger_user_info.get('phone')
            person_num = WorkRoute.get('person_num')
            plan_start_time = trsf_time(WorkRoute.get('plan_start_time'))
            price = WorkRoute.get('price')
            priceText = WorkRoute.get('priceText')
            thanks_price = WorkRoute.get('thanks_price')
            to_poi = WorkRoute.get('to_poi')
            t_business = to_poi.get('business')
            t_city = to_poi.get('city')
            t_city_name = t_city.get('city_name')
            t_provice_name = t_city.get('province_name')
            t_latitude = to_poi.get('latitude')
            t_longitude = to_poi.get('longitude')
            t_long_address = to_poi.get('long_address')
            t_short_address = to_poi.get('short_address')
            t_street = to_poi.get('street')
            WorkRouteInfo = {
                "create_time": create_time,
                "distance": distance,
                "driver_received_price": driver_received_price,
                "from_poi": {
                    "business": f_business,
                    "city": {
                        "city_name": f_city_name,
                        "province_name": f_provice_name
                    },
                    "latitude": f_latitude,
                    "long_address": f_long_address,
                    "longitude": f_longitude,
                    "short_address": f_short_address,
                    "street": f_street
                },
                "id": id,
                "passenger_user_info": {
                    "cid": cid,
                    "gender": gender,
                    "name": name,
                    "phone": phone,
                },
                "person_num": person_num,
                "plan_start_time": plan_start_time,
                "price": price,
                "priceText": priceText,
                "thanks_price": thanks_price,
                "to_poi": {
                    "business": t_business,
                    "city": {
                        "city_name": t_city_name,
                        "province_name": t_provice_name
                    },
                    "latitude": t_latitude,
                    "long_address": t_long_address,
                    "longitude": t_longitude,
                    "short_address": t_short_address,
                    "street": t_street
                },
            }
            print(WorkRouteInfo)
            insert_workroute(WorkRouteInfo)

    if cityroute_url1 in flow.request.url or cityroute_url2 in flow.request.url:
        text = flow.response.content
        text = json.loads(text)
        CityRouts = text.get('list')
        for CityRout in CityRouts:
            id = CityRout.get('id')
            from_poi = CityRout.get('from_poi')
            f_longitude = from_poi.get('longitude')
            f_latitude = from_poi.get('latitude')
            f_short_address = from_poi.get('short_address')
            f_long_address = from_poi.get('long_address')
            f_provice_name = from_poi.get('city').get('province_name')
            f_city_name = from_poi.get('city').get('city_name')
            f_business = from_poi.get('business')
            f_street = from_poi.get('street')
            to_poi = CityRout.get('to_poi')
            t_longitude = to_poi.get('longitude')
            t_latitude = to_poi.get('latitude')
            t_short_address = to_poi.get('short_address')
            t_long_address = to_poi.get('long_address')
            t_provice_name = to_poi.get('city').get('province_name')
            t_city_name = to_poi.get('city').get('city_name')
            t_business = to_poi.get('business')
            t_street = to_poi.get('street')
            price = CityRout.get('price')
            driver_received_price = CityRout.get('driver_received_price')
            thanks_price = CityRout.get('thanks_price')
            plan_start_time = trsf_time(CityRout.get('plan_start_time'))
            create_time = trsf_time(CityRout.get('create_time'))
            passenger_user_info = CityRout.get('passenger_user_info')
            cid = passenger_user_info.get('cid')
            name = passenger_user_info.get('name')
            gender = passenger_user_info.get('gender')
            CityRoutInfo = {
                "id": id,
                "from_poi": {
                    "longitude": f_longitude,
                    "latitude": f_latitude,
                    "short_address": f_short_address,
                    "long_address": f_long_address,
                    "city": {
                        "province_name": f_provice_name,
                        "city_name": f_city_name
                    },
                    "business": f_business,
                    "street": f_street
                },
                "to_poi": {
                    "longitude": t_longitude,
                    "latitude": t_latitude,
                    "short_address": t_short_address,
                    "long_address": t_long_address,
                    "city": {
                        "province_name": t_provice_name,
                        "city_name": t_city_name
                    },
                    "business": t_business,
                    "street": t_street
                },
                "price": price,
                "driver_received_price": driver_received_price,
                "thanks_price": thanks_price,
                "plan_start_time": plan_start_time,
                "create_time": create_time,
                "passenger_user_info": {
                    "cid": cid,
                    "name": name,
                    "gender": gender
                },

            }
            print(CityRoutInfo)
            insert_cityroute(CityRoutInfo)
