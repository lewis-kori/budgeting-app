from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateAPIView)

from tenants.models import Department

from ...models import Budget
from ..serializers.budget import BudgetDetailSerializer, BudgetSerializer


class BudgetListCreateAPIView(ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BudgetDetailSerializer
        return super().get_serializer_class()


class BudgetRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BudgetDetailSerializer
        return super().get_serializer_class()


# departmental budgets
class DepartmentalBudgetsListAPIView(ListAPIView):
    serializer_class = BudgetDetailSerializer

    def get_queryset(self):
        department = Department.objects.get(id=self.kwargs['department_id'])
        departmental_budgets = department.budgets.all()
        return departmental_budgets
