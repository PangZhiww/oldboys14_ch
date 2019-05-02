# from 模块倒入的专题练习2.core import main
# main.entry_point()

import sys
# print(__file__) # D:/practice/Python/oldboys14/day24/模块倒入的专题练习2/bin/start.py

ret = __file__.split("/")
# print(ret)
# ret.pop()
# ret.pop()
# print(ret[:-2])
bass_path = '/'.join(ret[:-2])
# print(bass_path)    # D:/practice/Python/oldboys14/day24/模块倒入的专题练习2
sys.path.append(bass_path)
from core import main