from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField()
    deposit_option_list = models.TextField(blank=True, null=True)
    saving_option_list = models.TextField(blank=True, null=True)

    nick_name = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    money = models.FloatField(null=True)
    salary = models.FloatField(null=True)

    def __str__(self):
        return self.username