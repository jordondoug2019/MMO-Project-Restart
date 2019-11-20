from rest_framework import serializers
from .models import UserModel, ShopModel, MonsterModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = '__all__'


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterModel
        fields = '__all__'
