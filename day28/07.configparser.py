import configparser

# file类型
# f = open("setting")

# 有一种固定格式的配置文件
# 有一个对应的模块去帮你做这个文件的字符串处理

# setterings.py 配置

# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11': 'yes'
#                      }
# config["bitbucket.org"] = {"User": "hg"}
# config["topsecret.server.com"] = {"Host Port": "50022",
#                                   "ForwardX11": "no"
#                                   }
#
# with open("example.ini","w") as f:
#     config.write(f)

config = configparser.ConfigParser()
# print(config.sections())
config.read("example.ini")
# print(config.sections())
# print("bytebong.com" in config)
# print("bitbucket.org" in config)
# print(config["bitbucket.org"]["user"])
# print(config["topsecret.server.com"]["forwardx11"])
# print(config["bitbucket.org"]["compressionlevel"])
# for key in config["topsecret.server.com"]:
#     print(key)
# print(config.options("topsecret.server.com"))
# print(config.items("topsecret.server.com"))
# print(config.get("topsecret.server.com","compression"))
config.add_section("yuan")
config.remove_section("bitbucker.org")
# config.remove_option("topsecret.server.com","forwardx11")
# config.set("topsecret.server.com","k1","v1")
# config.set("topsecret.server.com","forwardx11","11")
# config.set("yuan","k2","v2")
# config.set("yuan","k3","v3")
config.write(open("new2.ini","w"))