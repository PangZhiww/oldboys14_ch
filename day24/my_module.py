__all__ = ["login","name"]

# print("饿了么")
name = "alex"

def login():
    print("login",name)

import sys
# my_module = sys.modules["__main__"]
my_module = sys.modules[__name__]
getattr(my_module,"login")()

#1373
# import sys
# print(__name__)
# print("*****",sys.modules["__main__"])
# print(sys.modules)

if __name__ == "__main__":
    print("饿了么")
    print(__name__,type(__name__))


# print(__name__,type(__name__))   # __main__/my_module
# name = "egon"
# print("不饿")





# import sys
# my_module = sys.modules[__name__]
# getattr(my_module,"login")()

# import sys
# print(__name__)
# print("*****",sys.modules["__main__"])
# print(sys.modules)

# if __name__ == "__main__":
#     print("饿了么")
#     print(__name__,type(__name__))  # "__main"/"my_module"
# name = "egon"
# print("不饿")