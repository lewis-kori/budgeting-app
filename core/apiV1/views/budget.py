from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from ...models import Budget
from tenants.models import Department
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
