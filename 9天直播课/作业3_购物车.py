goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

import getpass
import os

_username = input("Username:").strip()
_password = getpass.unix_getpass("Password:")

filename = "db/%s" % _username
if os.path.isfile(filename):
    f = open(filename, "r")
    data = eval(f.read())
    if _username == data["account"]["username"] and _password == data["account"]["password"]:
        while 1:
            for index, i in enumerate(goods):
                print(index, i["name"], i["price"])
            choice = input("请选择商品:").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= 0 and choice < len(goods):
                    p = goods[choice]
                    if data["balance"] >= p["price"]:
                        data["shop_cart"].append(p)
                        data["blance"] = data["blance"] - p["price"]
                        print("添加了[%s]到你的购物车, 还有余额\003[31;1m[%s]\003[0m" % (p["name"], data["balance"]))
                    else:
                        print("买不起, 留下来穷人的眼泪...")
            elif choice == "quit":
                print("已购买商品".center(50, "*"))
                for i in data["shop_cart"]:
                    print(i)
                f = open(filename, "w")
                f.write(str(data))
                f.close()
                exit("还有余额: %s" % data["balance"])
            else:
                print("输入不合法!")
    else:
        print("用户名或密码错误! 请重新输入")
        # continue
else:
    print("用户不存在!")
