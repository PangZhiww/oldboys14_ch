# lst = ["周杰伦","王力宏","周润发"]
# lst.append("五百")  # 向列表中添加一个元素, 元素放在末尾. 把一个元素追加到列表的末尾
# print(lst)
# lst.append("周星星")
# print(lst)
# lst.insert(4,"马化腾")   # 把元素插入到指定位置. 元素的移动
# print(lst)
# lst.extend(["马云","王健林","李嘉诚"])    # 迭代添加
# print(lst)

# lst = []
# while True:
#     name = input("请输入学生的名字:")
#     if name.upper() == "Q":
#         break
#     else:
#         lst.append(name)    # 把名字添加到列表
# print(lst)

# lst = ["盖伦","大白梨","提莫","大白梨"]
# 1.pop()
# e = lst.pop()    # 返回删除的元素, 删除最后一个
# print(e)
# print(lst)
# e = lst.pop(1)      # 根据给出的索引进行删除
# print(e)
# print(lst)

# lst.remove("提莫")
# lst.remove("大白梨")
# lst.remove("大白梨")
# print(lst)

# 3. del 删除 切片删除     delete
# del lst[1::2]
# print(lst)

# lst.clear()
# print(lst)


# lst = ["麻花藤", "王剑林林", "李李嘉诚", "王富贵"]
# print(lst)
# deleted = lst.pop()  # 删除最后⼀一个
# print("被删除的", deleted)
# print(lst)

# lst = ["王志⽂文", "张⼀一⼭山", "苦海海⽆无涯"]
# lst.extend(["麻花藤", "麻花不不疼"])
# print(lst)


lst = ["太白", "五色", '银王', '日天','白天',"的金凤凰","打南门口","㝉好好","太白", "五色", '银王', '日天','白天',"的金凤凰","打南门口","㝉好好"]
# lst[2] = "金角大王"
# print(lst)
# lst[0] = "太黑"
# print(lst)
lst[1:3] = "马"
print(lst)
# lst[1:3] = "马化"
# print(lst)
# lst[1:3] = "马化腾"
# print(lst)
# lst[1:3] = ["周杰伦","他媳妇","王力宏她媳妇"]
# print(lst)
# lst[1:12:3] = ["马化腾","哇靠","打的","地方"]
# print(lst)

# for el in lst:
#     print(el)       # element


# lst = ["王尼玛","我记着你","炜哥","放学后天台见","王尼玛","王尼玛"]
# print(len(lst))
# print(lst.count("王尼玛"))

# lst = [1,5,786,95,6124,3,53,65,89,41]
# lst = ["王尼玛","我记着你","56","炜哥","放学后天台见","王尼玛","王尼玛"]
# lst.sort()      # 升序
# lst.sort(reverse = True)    # 倒序
# lst.reverse()   # 反转
# print(lst)
# list
