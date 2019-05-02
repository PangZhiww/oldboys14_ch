# lst = ["马化腾",'麻花藤','马云','中红衣']
# print(lst[0])
# print(lst[1])
# print(lst[2])
# lst[3] = ["流动性",'发的']
# print(lst)

# lst = ["啊花藤","王健林",'马云','周鸿祎',"向华强"]
# print(lst[0:3])
# print(lst[:3])
# print(lst[1:2])
# print(lst[2::-1])
# print(lst[-1:-4:-2])

# lst = ["麻花藤", "林林俊杰", "周润发", "周芷若"]
# print(lst)
# lst.append("wusir")
# print(lst)

# lst = []
# while True:
#     content = input("请输入你要录入的员工信息,输入Q退出:")
#     if content.upper() == 'Q':
#         break
#     lst.append(content)
# print(lst)

# lst = ["麻花藤", "张德忠", "孔德福"]
# lst.insert(1,"刘德华")
# print(lst)

# lst = ["王志⽂文", "张⼀一⼭山", "苦海海⽆无涯"]
# lst.extend(["麻花藤","麻花不疼"])
# print(lst)

# lst = ["麻花藤", "王剑林林", "李李嘉诚", "王富贵"]
# print(lst)
# deleted = lst.pop()
# print(deleted)
# print(lst)

# el = lst.pop(2)
# print(el)
# print(lst)

# lst.remove("麻花藤")
# print(lst)

# lst.clear()
# print(lst)

# del lst[1:3]
# print(lst)


# lst = ["太⽩白", "太⿊黑", "五⾊色", "银王", "⽇日天","短发的"]
# lst[1] = "太污"
# print(lst)

# lst[1:6:2] = ["麻花藤",'哇靠','发斯蒂芬']
# print(lst)
#
# lst[1:4] = ["李嘉诚个龟儿子"]
# print(lst)

# for el in lst:
#     print(el)

# lst = ["太白",'太黑','五色','银王','日天','太白']
# c = lst.count("太白")
# print(c)

# lst = [1, 11, 22, 2]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = ["太白",'太黑','五色','银王','日天','太白']
# print(lst)
# lst.reverse()
# print(lst)
# l = len(lst)
# print(l)


#  列表的嵌套
# lst = [1,'太白','ausir',['马马虎虎',['可口可乐'],'王健林']]
# print(lst[2])
# print(lst[3])
# print(lst[1:3])
# print(lst[1][1])
# s = lst[2]
# s = s.capitalize()
# lst[2] = s
# print(lst)
# lst[1] = lst[1].replace("白",'黒')
# print(lst)
# print(lst[3][0][3])
# lst[3][0] = lst[3][0].replace("虎",'化')
# print(lst)
# lst[3].append("雪碧")
# lst[3][1].append("雪碧")
# print(lst)


#  元祖和元祖嵌套
# tu = (1, '太白','李白',"太黑","怎么黑")
# print(tu)
# print(tu[2])
# print(tu[2:5])
# for el in tu :
#     print(el)
# c = tu.count('李白')
# print(c)
# tu = (1,"哈哈",[],'喝喝')
# tu[2].append("马化腾")
# tu[2].append("王健林")
# print(tu)

# tu = ('1',)
# print(type(tu))


#  range
# for num in range(10):
#     print(num)
# for num in range(1,10,2):
#     print(num)
# for num in range(10,1,-2):
#     print(num)
# for num in range(-20,-10,2):
#     print(num)



#  作业
# li = ["alex",'WuSir','ritian','barry','wenzhou']
# sum = len(li)
# print(sum)
# li.append("seven")
# print(li)
# li.insert(0,'seven')
# print(li)
# li[1] = li[1].replace("WuSir","kelly")
# print(li)
# l2 = [1,'a',3,4,'heart']
# li.extend(l2)
# print(li)
#   第六题
# s = "qwert"
# li.extend(s)
# print(li)
#   第七题
#   第八题
# del li[2:4]
# print(li)
# li.reverse()
# print(li)
# print(li.count("alex"))


# li = [1,3,2,"a",4,"b",5,"c"]
# print(li[0:3])
# print(li[3:6])
# l3.sort()
# print(li)
# count = 1
# while count < 7:
#     if count % 2 == 1:
#         print(count)
#     else:
#         pass
#     count = count + 1
# l4 = li[1:6:2]
# print(l4)
# l5 = li[7:]
# print(l5)
# l6 = li[5:0:-2]
# print(l6)


#   第三大题
# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","adv"]
# lis[3][2][1][0] = lis[3][2][1][0].upper()   # 方法一
# lis[3][2][1][0] = lis[3][2][1][0].replace("t","T")
# print(lis)
# lis[3][2][1][0] = "TT"    # 第二种
# print(lis)
# lis[1] = str(lis[1] + 97)   # 第一种
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
# print(lis)
# lis[1] = "100"  # 第二种
# lis[3][2][1][1] = "100"
# print(lis)
# lis[3][2][1][2] = int(lis[3][2][1][2].replace("1","101"))   #  第一种
# lis[3][2][1][2] = 101     # 第二种
# print(lis)


#  第四题
# li = ["alex","enic","rain"]
# li = "alex{}enic{}rain" .format("_","_")
# s = ""
# for el in li:
    # s = s + el + "_"
# print(s)
# print(s[:len(s)-1])
# print(s[:-1])


#   第五题
# li = ["alex","WuSir","ritian","barry","wenzhou"]
# for num in li:
#     print(num)
# for num in range(len(li)):
#     print(num)


#   第六题
# lst = []
# for num in range(1,101):
#     if num % 2 == 0:
#         lst.append(num)
        # print(num)
# print(lst)

#   第七题
# lst = []
# for i in range(51):
#     if i % 3 == 0:
#         lst.append(i)
#     print(i)
# print(lst)

#   第八题
# lst = []
# for i in range(101):
#     lst.append(i)
    # print(i)
# lst.reverse()
# print(lst)

# for i in range(100,0,-1):
#     print(i)

# count = 100
# while count > 0:
#     print(count)
#     count = count - 1


#   第九题
# lst = []
# for i in range(100,9,-1):
#     if i % 2 == 0:
#         lst.append(i)
#
# new_lst = []
# for el in lst:
#     if el % 4 == 0:
#         new_lst.append(el)
# print(new_lst)


#   第十题
# lst = []
# for i in range(1,31):
#     lst.append(i)
#     print(i)
# print(lst)
#
# new_lst = []
# for el in lst:
#     if el % 3 == 0:
#         el = "*"
#         print(el)
    # new_lst.append(el)
# print(new_lst)


#   第十一题
# li = ["TaiBai","ale xC","AbC ","egon","ri Tian","WuSir"," apc"]
# lst = []
# for el in li:
#     el = el.replace(" ","")
#     if (el.startswith("A") or el.startswith("a")) and el.endswith("c"):
#         lst.append(el)
# print(lst)


#   第十二题
# lst = []
# li = ["苍老师","东京热","武藤兰","波多野结衣"]
# content = input("请输入你的评论:")
# for el in li:
#     if el in content:
#         content = content.replace(el,"*" * len(el))
# # print(content)
# lst.append(content)
# print(lst)


#   第十三题
# li = [1,3,4,"alex",[3,7,8,"TaiBai"],5,"RiTiAn"]
# for e in li:
#     # print(e)
#     if type(e) == list:     #   判断e的数据类型
#         for ee in e:
#             if type(ee) == str:
#                 print(ee.lower())
#             else:
#                 print(ee)
#     else:
#         if type(e) == str:
#             print(e.lower())
#         else:
#             print(e)


#   第十四题
# lst = []
# while 1:
#     stu = input("请输入学生的姓名和成绩(姓名_成绩)(*输入Q退出录入):")
#     if stu.upper() == "Q":
#         break
#     lst.append(stu)
# print(lst)
#   求平均值
# sum = 0
# for el in lst:
#     print(el)
    # li = el.split("_")
    # print(li)
    # sum = sum + int(li[1])
# print(sum/len(lst))
