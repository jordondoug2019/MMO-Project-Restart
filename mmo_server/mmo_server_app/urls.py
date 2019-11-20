from rest_framework import routers
from django.urls import include, path
from .api import UserViewSet, MonsterViewSet, ShopViewSet
from . import views

router = routers.DefaultRouter()

router.register('users',UserViewSet)
# router.register('newuser', NewUserViewSet)
router.register('monsters', MonsterViewSet)
router.register('shop', ShopViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('user_auth', views.user_auth, name='user_auth')]