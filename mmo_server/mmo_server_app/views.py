from django.shortcuts import render
from json import loads
from .models import UserModel, ShopModel, MonsterModel
from django.http import HttpResponse


# Create your views here.
def user_auth(request):
    requestInfo = loads(request.body)

    userInfo = UserModel.objects.filter(username=requestInfo['username'])

    if (userInfo):
        if userInfo[0].password == requestInfo['password']:
            return HttpResponse(userInfo[0].id)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse(False)
