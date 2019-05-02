# class Alipay:
#     def __init__(self,money):
#         self.money = money
#     def pay(self):
#         print("使用支付宝了%s" % (self.money))
#
# class Jdpay:
#     def __init__(self,money):
#         self.money = money
#
#     def pay(self):
#         print("使用京东支付了%s" % (self.money))
#
# a1 = Alipay(200)
# a1.pay()
# j1 = Jdpay(100)
# j1.pay()

# class Alipay:
#     def __init__(self,money):
#         self.money = money
#     def pay(self):
#         print("使用支付宝支付了%s" %(self.money))
# class Jdpay:
#     def __init__(self,money):
#         self.money = money
#     def pay(self):
#         print("使用京东支付了%s" % (self.money))
# def pay(ob):
#     ob.pay()
# a1 = Alipay(200)
# j1 = Jdpay(100)
# print(a1)
# print(j1)
# pay(a1)
# pay(j1)


from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):pass
    @abstractmethod
    def func(self):pass

class Alipay(Payment):
    def __init__(self,money):
        self.money = money
    def pay(self):
        print("使用支付宝支付了%s" % self.money)
class Jdpay(Payment):
    def __init__(self,money):
        self.money = money
    def pay(self):
        print("使用京东支付了%s" % self.money)
class Wechatpay(Payment):
    def __init__(self,money):
        self.money = money
    def pay(self):
        print("使用微信支付了%s" % (self.money))
def pay(obj):
    obj.pay()
# w1 = Wechatpay(200)
# a1 = Alipay(300)
# j1 = Jdpay(100)
# pay(a1)
# pay(j1)
# w1 = Wechatpay(500)
# pay(w1)
print(pay(Wechatpay(100)))