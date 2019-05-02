# lst = ['alex','sb','taibai','sb','wusir','sb','ritian','sb']

# new_lst = [i.upper() for i in lst if len(i)>=3]
# print(new_lst)

# lst = [(x,y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 == 1]
# print(lst)

# M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([i[2] for i in M])

# M = [3,6,9]
# print([[x-2,x-1,x] for x in M])


# print([x*x for x in range(51) if x % 3 == 0]).


# print([(s,s+1) for s in range(6)])


# print([x for x in range(20) if x % 2 == 0])
# print([x for x in range(0,20,2)])


# li = ['alex','wusir','laonanhai','taibai']
# print([li[i] + str(i) for i in range(len(li))])


x = {
    'name':'alex',
    'Values':[{'timestamp':1517991992.94,'values':100},
    {'timestamp':1517991992.94,'values':200},
    {'timestamp':1517991992.94,'values':300},
    {'timestamp':1517991992.94,'values':350},
    {'timestamp':1517991992.94,'values':280},
    ]
}
print([[el['timestamp'],el['values']] for el in x['Values']])