from django.contrib import admin

from .models import Account, Budget, Expense

# Register your models here.
admin.site.register(Account)
admin.site.register(Budget)
admin.site.register(Expense)