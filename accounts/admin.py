from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserBankAccount, UserAddress

# Register your models here.
admin.site.register(UserBankAccount)
admin.site.register(UserAddress)