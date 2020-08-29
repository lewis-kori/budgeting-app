from rest_framework.serializers import ModelSerializer

from ...models import Expense
from .budget import BudgetDetailSerializer


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseDetailSerializer(ModelSerializer):
    budget = BudgetDetailSerializer()

    class Meta:
        model = Expense
        fields = '__all__'
