from django.http import JsonResponse
from frontEnd.models import *


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