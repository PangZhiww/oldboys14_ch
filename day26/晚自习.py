# import re
# ret = re.search(r"\d+(\.\d+)(\d)",r"1.23+2.3+3-4*5")
# print(ret.group())
# print(ret.group(1))
# # print(ret.group(2))
# # print(ret.group(3))
# print(ret.groups())

import re
ret = re.split(r"\d+(\w+)","18191d919df151erd59f1e41")
print(ret)