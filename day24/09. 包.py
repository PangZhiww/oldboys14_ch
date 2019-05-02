# import glance.api.policy    # 第一个点左边永远是一个包的名字
# glance.api.policy.get()

# 简化方法
# import glance.api.policy as policy   # 第一个点左边永远是一个包的名字
# policy.get()


# from glance.api import policy
# policy.get()



# 导入包   相当于执行了这个包下面的__init__.py
# 设计一下init文件来完成一些模块的导入
# aaa.glance.api.policy.get()
# aaa.glance.db.models.register_models()




# 相对导入
from aaa import glance2
glance2.api.policy.get()