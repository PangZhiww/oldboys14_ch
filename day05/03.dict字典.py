# dict = {'jay':'周杰伦','jj':'林俊杰','Eason':'陈奕迅'}
# print(dict)
# dict = {1:"马化腾",False:"阿里巴巴","sylar":"帅的不行不行的",(1,"哈哈"):"元祖"}#,["吼吼"]:"列表"}
# print(dict)

#  字典的相关操作
#   增加
# dict = {"昆凌":"周杰伦的老婆"}
# dict["国际章"] = "汪峰的老婆"     #  新增
# dict["国际章"] = "雄壮的老外"     #  如果key重复了,会替换掉原来的value

# dict.setdefault("马蓉","王宝强的前任老婆")
# dict.setdefault("马蓉","宋哲的现任老婆")     #  如果字典中已经包含了这个key, 不再继续保存
# print(dict)


#   删除
dict = {"牌牌":"你去哪里了","晓雪":"你快回来","雪雪":"又走了"}
dict.pop("晓雪")
# ret = dict.pop("晓雪")      #   删除一个元素,返回这个元素的value值
# print(ret)

# del dict["牌牌"]    #  没有返回值
# ret = dict.popitem()    #  随机删除  返回给你的是一个元组
# print(ret)
print(dict)


#   修改
# dict = {'jay':'周杰伦','jj':'林俊杰','Eason':'陈奕迅'}
# dict1 = {"牌牌":"你去哪里了",'jay':'杰伦',"晓雪":"你快回来","雪雪":"又走了"}
# dict.update(dict1)
# print(dict)
# print(dict1)

# dict = {"id":1,"name":"李嘉诚","money":10000}
# dict["money"] = dict["money"] - 500     #  用key去修改
# print(dict)


#   查询
# dict = {"及时雨":"松江","小李广":"华容","黑旋风":"李逵","易大师":"剑圣"}
# dict["大宝剑"] = "盖伦"    #  新增
# dict["及时雨"] = "天老爷"    #   修改
# print(dict["易大师"])    #  查询
# print(dict["易大师是个脑残"])     #  查询,如果key不存在,报错
# print(dict.get("易大师是个脑残"))    #  如果key不存在,返回None
# print(dict.get("易大师是个脑残","余小c"))    #  可以通过key来获取value的值,那么如果key不存在,返回None:同时可以给出一个默认值,当key不存在的时候返回默认值
# print(dict)

# dict = {"及时雨":"松江","小李广":"华容"}
# dict.setdefault("及时雨")
# dict.setdefault("及时雨","萨克斯")
# ret = dict.setdefault("及时雨")
# print(ret)
# ret = dict.setdefault("及时雨123","hello")     #  没有的可以帮助我们添加
# ret = dict.setdefault("及时雨123")     #  没有的返回None
# print(ret)
# print(dict)
# 1. 首先判断原来的字典中用没有这个key.如果没有,则执行新增
# 2. 用这个key去字典中查询,返回查询到的结果