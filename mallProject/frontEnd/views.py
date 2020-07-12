from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from frontEnd.view.users import *
from frontEnd.view.orders import *
from frontEnd.view.shoppingCarts import *
from frontEnd.view.configurAddressee import *
from frontEnd.view.gets import *
