from django.db import models
import random


# Create your models here.
def random_health():
    return random.randint(100, 301)


def random_attack():
    return random.randint(15, 46)


class UserModel(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10, null=True)
    userImage = models.URLField(null=True, blank=True)
    healthPoints = models.IntegerField(null=True, blank=True, default=random_health())
    attackPoints = models.IntegerField(null=True, blank=True, default=random_attack())
    weapon = models.CharField(max_length=40, null=True)
    weaponAttack = models.IntegerField(null=True, blank=True)
    weaponHealth = models.IntegerField(null=True, blank=True)


class ShopModel(models.Model):
    weaponName = models.CharField(max_length=20)
    shopHealthPoints = models.IntegerField()
    shopAttackPoints = models.IntegerField()


class MonsterModel(models.Model):
    monsterImage = models.URLField()
    monsterHealthPoints = models.IntegerField()
    monsterAttackPoints = models.IntegerField()
