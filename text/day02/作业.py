# count = 1
# n = 66
# while count <= 3:
#     num = input("你猜一下:")
#     if int(num) > n:
#         print("猜大了")
#     elif int(num) < n:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break



# import requests,time
# for i in range(1000):
#     header = {'Host': 'business-rest.01zhuanche.com', 'Connection': 'keep-alive', 'Content-Length': '17',
#               'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'https://vip.01zhuanche.com',
#               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#               'Referer': 'https://vip.01zhuanche.com/login.html', 'Accept-Encoding': 'gzip, deflate, br',
#               'Accept-Language': 'zh-CN,zh;q=0.9',
#               'Cookie': 'Hm_lvt_44b89a2108eb84a48ec1b4f686af2753=1534215037; Hm_lpvt_44b89a2108eb84a48ec1b4f686af2753=1534215037'}
#
#     data = 'phone=18720940250'
#     url = 'http://business-rest.01zhuanche.com/api/v1/company/smsSend'
#     res = requests.post(url=url, headers=header, data=data)
#     time.sleep(301)

count = 1
while count <= 10:
    if count != 7:
        print(count)
    count = count + 1