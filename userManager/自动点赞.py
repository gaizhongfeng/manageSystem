import requests
# 1.首先登陆任何页面，获取cookie
i1 = requests.get(url="http://dig.chouti.com/help/service")

# 2.用户登录，携带上一次的cookie，后台对cookie中的gpsd进行授权
i2=requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone':"86手机号",
        'password':"密码",
        'oneMonth':"",
        },
    cookie = i1.cookies.get_dict()
    )

# 3.点赞， 只需携带已被授权的gpsd即可
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=",
    cookies = {'gpsd':gpsd}
)
print(gpsd)