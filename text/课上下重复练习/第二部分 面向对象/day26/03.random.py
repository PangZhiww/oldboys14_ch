import random


def rand_code(n=6, alph_flag=True):
    code = ""
    for i in range(n):
        rand_num = str(random.randint(0, 9))
        if alph_flag:
            rand_alph = chr(random.randint(97, 122))
            rand_alph_upper = chr(random.randint(65, 90))
            rand_num = random.choice([rand_num, rand_alph, rand_alph_upper])
        code = code + rand_num
        return code


ret = rand_code(n=4, alph_flag=True)
print(ret)
