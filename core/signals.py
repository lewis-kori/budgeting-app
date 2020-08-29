from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Budget, Expense


@receiver(pre_save, sender=Expense)
def subtract_expense_from_budget(sender, instance, *args, **kwargs):
    budget = instance.budget

    budget.amount -= instance.amount
    budget.save()


@receiver(post_save, sender=Budget)
def subtract_from_account(sender, instance, created, **kwargs):
    if created:
        account = instance.source
        account.amount -= instance.amount
        account.save()