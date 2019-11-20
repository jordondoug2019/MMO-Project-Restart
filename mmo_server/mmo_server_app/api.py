from .models import UserModel, ShopModel, MonsterModel
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, MonsterSerializer, ShopSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = ShopModel.objects.all()
    serializer_class = ShopSerializer


class MonsterViewSet(viewsets.ModelViewSet):
    queryset = MonsterModel.objects.all()
    serializer_class = MonsterSerializer
