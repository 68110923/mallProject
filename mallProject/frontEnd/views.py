from django.http import JsonResponse
from frontEnd.table import *



class gets:
    def __init__(self,request):
        self.request = request
    def index(self):
        return JsonResponse({
            '用户信息':'b',
            '商品信息':'b',
        })
    def commodityDetailedInfo(self):
        return JsonResponse({})



class users:
    def __init__(self,request):
        self.request = request

    # 登录login
    def login(self):
        return JsonResponse({'个人资料':''})

    def user(self):
        # 查看用户(他人)信息
        if self.request.method == 'GET':
            return JsonResponse({'个人资料':''})
        # 注册register
        elif self.request.method == 'POST':
            return JsonResponse({'个人资料':''})
        # 修改个人资料modification
        elif self.request.method == 'PUT':
            return True
        # 注销账户
        elif self.request.method == 'DEL':
            return True

    # 查看个人资料
    def getPersonalMessage(self):
        return JsonResponse({'个人资料':''})

    # 修改密码
    def modifyPassword(self):
        return True

    # 修改头像
    def modifyAvatar(self):
        return JsonResponse({'头像地址':''})

    # 绑定手机号码
    def bindingTelNumber(self):
        return True

class configurAddressee:
    def __init__(self,request):
        self.request = request

    def addressee(self):
        # 新增收件人
        if self.request.method == 'POST':
            return True

        # 获取收件人列表
        elif self.request.method == 'GET':
            return JsonResponse({})

        # 修改收件人信息
        elif self.request.method == 'PUT':
            return True

        # 删除收件人信息
        elif self.request.method == 'DEL':
            return True

    # 设置收件人信息为默认
    def defaultAaddressee(self):
        return True


class shoppingCarts:
    def __init__(self,request):
        self.request = request

    def cart(self):
        # 加入购物车
        if self.request.method == 'POST':
            return True

        # 修改数量
        elif self.request.method == 'PUT':
            return True

        # 删除
        elif self.request.method == 'DEL':
            return True

        # 查看购物车列表
        elif self.request.method =='GET':
            return JsonResponse({})

class orders:
    def __init__(self,request):
        self.request = request

    def order(self):
        # 查看订单信息
        if self.request.method == 'GET':
            return JsonResponse({})

        # 删除订单信息
        elif self.request.method == 'DEL':
            return True

        # 订单结束后的评价功能
        elif self.request.method == 'POST':
            return True

    # 结算(模仿淘宝结算功能)
    def settlement(self):
        pass

    # 提交订单，提交订单后直接跳转到支付页面
    def addOrder(self):
        return True

    # 取消订单
    def cancelOrder(self):
        return True

    # 支付功能
    def pay(self):
        return True






