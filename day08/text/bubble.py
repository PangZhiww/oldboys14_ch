lst = [1,18,16,2,5,77,6,25,24.37,99]
    # 通过交换的方式, 把列表中的最大的值移动到最右端
for abc in range(len(lst)):     # 控制内部移动的次数
    n = 0
    while n < len(lst) - 1:
        if lst[n] > lst[n+1]:
            lst[n],lst[n+1] = lst[n+1],lst[n]
        else:
            pass
        n = n + 1
print(lst)

