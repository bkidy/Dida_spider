
import urllib.parse
import urllib.request

url = 'http://211.151.134.222/V3/BookingDriver/getNearbyBookingRideList'
headers = {
    'Host':'211.151.134.222',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'PHPSESSID=rvn3vcpcms3dgc6sagj7855cn0',
    'Connection':'keep-alive',
    'ddcinfo':'ehAq+CFEfF1shstO1x8aie3K7NbKTAJHam/3Ve7fkYl0nYGvCuXWcNZRqZKQqU+/DVpLJPMkX3HPlSCtYDlSeSW8EkwaxGTl3hR3N4jn/347n0qNUJYpwSWKbIZJk2mNsactl1XRqDxnq11Vn4Q7ZlEsFRXWi9lfq2f8nGuHeGQb4Vii+S8HdpGDALAOVdliukBagUDJcRQN01Df5WorQ/rForerOVeZ2i5v2XwX1K+UL1F0kUNeHBwh6SR49WigFcVaGp49kGQOuBfS++37+oxt2zGonl6lPzwr4bYFJ+65BgLwrluS2m3f+ZSRWaaLO7hPXd/UdexhnwvQomyb5c9IRLLjgBaTvyEFJ8SHTdzfLjvYbRRYspnc0j8fgUyXKmKxJa8JI8mChg2fQA44Gn8CyUrweTwOp3hkCrzh/Ax3pML7Jg80goSbgBhopvilRzXfTlIgY/WkZiKbVEUV9Q5zhvYZ/nFUk4srxMUCaEc=',
    'Proxy-Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'DidaPinche/8.0.6(iOS 12.0.1;iPhone9,2) DidaPinche/8.0.6 dc(eydsYXQnOjMwLjE4ODkyMCwnbG9uJzoxMjAuMjMxMzcwfQ==) (iOS 12.0.1;iPhone9,2) Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404',
    'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9, io-CN;q=0.8',
    'Content-Length':'340',
    # 'Accept-Encoding':'gzip, deflate'
}
postdata = urllib.parse.urlencode({
    "actid":"dida_app",
    "center_latitude":"30.189050",
    "center_longitude":"120.231430",
    "filter_by":"all",
    "mobiletype":"1",
    "order_by":"default",
    "page":"1",
    "page_size":"20",
    "ride_type":"3",
    "sig": "3010ef255241255cef06a44d92a123bf",
    "token": "65411eef-0aae-4b0e-bfb0-b54a15d20538",
    "ts":"20181214225230",
    "user_cid":"b6fea50c-41d6-4fc0-a779-8c1cd8533bba",
    "version":"8.0.6",
    "vkey":"9472DCE5260AA89BC6A8C481C4489F56",
}).encode('utf-8')

req = urllib.request.Request(url,postdata,headers)
r = urllib.request.urlopen(req)
print(r.read().decode('utf-8'))