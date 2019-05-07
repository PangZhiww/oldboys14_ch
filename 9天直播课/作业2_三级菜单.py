menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
layers = [menu,]
print(layers)
while 1:
    if len(layers) == 0:break
    courrent_layers = layers[-1]
    for key in courrent_layers: # 打印菜单中的内容
        print(key)
    choice = input("请输入你想要选择的地址: ").strip().upper()
    if choice == "B":
        layers.pop(-1)
        continue    # 返回上一级菜单
    if choice == "Q":break  # 结束这次循环
    if choice not in courrent_layers:
        print("您输入的不合法,请重新输入:")
        continue    # 重新进行输入循环
    count = layers.append(courrent_layers[choice])
    # if count not in courrent_layers:
    #     print("最后一级菜单, 没有内容.请输入B返回上一级菜单; 或者输入Q结束菜单选择")   # 避免多次输入没有下一级菜单