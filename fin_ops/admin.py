from django.contrib import admin
from .models import MoneyAccount, CurrencyType, FinOperation, Category


# Register your models here.
admin.site.register(MoneyAccount)
admin.site.register(CurrencyType)
admin.site.register(FinOperation)
admin.site.register(Category)