from django.db import models
from django.utils.dates import MONTHS
from tenants.models import CommonInfo, Department

# Create your models here.


# accounts info page
class Account(CommonInfo):
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField(
        help_text='amount currently in the account stated')

    def __str__(self):
        return self.name


# budget allocated to each department.
class Budget(CommonInfo):
    department = models.ForeignKey(Department,
                                   related_name='budgets',
                                   on_delete=models.PROTECT)
    source = models.ForeignKey(Account,
                               related_name='budgets',
                               on_delete=models.PROTECT)
    month = models.PositiveSmallIntegerField(choices=MONTHS.items())
    year = models.PositiveIntegerField()
    amount = models.BigIntegerField(
        help_text='allocation amount for the department')

    def __str__(self):
        return f'{self.department}: month- {self.get_month_display()} {self.amount}'


class Expense(CommonInfo):
    budget = models.ForeignKey(Budget,
                               related_name='expenses',
                               on_delete=models.PROTECT)
    date = models.DateField()
    use = models.TextField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.use} {self.amount}'