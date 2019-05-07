red_ball = []
blue_ball = []
while len(red_ball) < 6:
    red_num = int(input("请输入红球的数字(1-32为合法球号):"))
    if red_num in range(33) and red_num not in red_ball:
        red_ball.append(red_num)
    else:
        print("输入不合法!")
        continue
while len(blue_ball) < 2:
    blue_num = int(input("请输入蓝球的数字(1-16为合法球号):"))
    if blue_num in range(17) and blue_num not in blue_ball:
        blue_ball.append(blue_num)
    else:
        print("输入不合法!")
        continue
print("红球为:", red_ball)
print("蓝球为:", blue_ball)