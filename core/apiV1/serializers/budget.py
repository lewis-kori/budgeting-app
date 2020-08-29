from rest_framework.serializers import ModelSerializer,SerializerMethodField

from ...models import Budget
from .account import AccountSerializer
from tenants.apiV1.serializers.departments import DepartmentSerializer

class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BudgetDetailSerializer(ModelSerializer):
    department = DepartmentSerializer()
    month = SerializerMethodField()
    source = AccountSerializer()
    class Meta:
        model = Budget
        fields = '__all__'

    def get_month(self, obj):
        return obj.get_month_display()
