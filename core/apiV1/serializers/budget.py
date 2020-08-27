from rest_framework.serializers import ModelSerializer,SerializerMethodField

from ...models import Budget
from .account import AccountSerializer


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BudgetDetailSerializer(ModelSerializer):
    month = SerializerMethodField()
    source = AccountSerializer()
    class Meta:
        model = Budget
        fields = '__all__'

    def get_month(self, obj):
        return obj.get_month_display()
