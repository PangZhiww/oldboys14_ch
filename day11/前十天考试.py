# int("11a")
# ret = '{0},{2}.{1}'.format('a','b','c')
# print(ret)

# print(5 and 0)

# 第九题
# lis = [['k',['qwe',{'k1':['tt',3,'1']},89],'ab']]
# lst= lis[0][1][1]['k1'][0].upper()
# print(lst)
# lis[0][1][1]['k1'][1]
# print(lis[0][1][1]['k1'][1])
# lis[0][1][1]['k1'][1] = str(lis[0][1][1]['k1'][1]+97)
# print(lis)
# lis[0][1][1]['k1'][2] = lis[0][1][1]['k1'][2]+'01'
# print(lis)


# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3):{'k3':['2',100,'wer']}}
# dic['k2'].append('23')
# print(dic)

# dic['k2'].insert(0,'a')
# print(dic)

# dic[(1,2,3)]['k4'] = 'v4'
# print(dic)


# 第十一题
# for i in range(100,-1,-1):
#     print(i)


# 四. 编程题
# 第二题
# dic = {"最终计算结果":None}
# content = input("请输入内容:").strip()
# lst = content.split('+')
# print(lst)
# sum = 0
# for el in lst:
#     sum = sum + int(el.strip())
# print(sum)
# dic['最终计算结果'] = sum
# print(dic)


# 第三题
# def main(file_path,*args):
#     s = '_'.join(args)
#     f = open(file_path,mode='a',encoding='utf-8')
#     f.write(s)
#     f.flush()
#     f.close()
#
# main('faa','adf','dfadf','adfa')


# 第四题
# def func(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         new_lst.append(lst[i] + str(i))
#     return new_lst

# lst = ['alex','taibai','五色']
# func(['alex','taibai','五色'])



# 有文件t1.txt里面的内容为：（6分）
#   1,alex,22,13651054608,IT
# 	2,wusir,23,13304320533,Tearcher
# 	3,taibai,18,1333235322,IT
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','	 		'job':'IT'},......]


# 第五题
# result = []
# with open('t1.txt',mode='r',encoding='utf-8') as f:
#     for line in f:
#         dic = {}
#         lst = line.split(',')
#         dic['id'] = lst[0].strip()
#         dic['name'] = lst[1].strip()
#         dic['age'] = lst[2].strip()
#         dic['phone'] = lst[3].strip()
#         dic['job'] = lst[4].strip()
#         result.append(dic)
#
# print(result)


# 第六题
# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     if row > 66:
#         result.setdefault('k1',[]).append(row)
#     else:
#         result.setdefault('k2',[]).append(row)
#
# print(result)



# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     if row > 66:
#         l = result.get('k1')    # 上来就拿K1
#         if l == None:   # K1不存在, 没有这个列表
#             result['k1'] = [row]    # 创建一个列表扔进去
#         else:   # K1如果存在
#             result['k1'].append(row)    # 追加内容
#     else:
#         l = result.get('k2')  # 上来就拿K1
#         if l == None:  # K1不存在, 没有这个列表
#             result['k2'] = [row]  # 创建一个列表扔进去
#         else:  # K1如果存在
#             result['k2'].append(row)  # 追加内容
#
# print(result)


# 第七题






