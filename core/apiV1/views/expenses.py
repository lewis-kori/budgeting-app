from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,ListAPIView

from ...models import Expense,Budget
from ..serializers.expenses import ExpenseDetailSerializer, ExpenseSerializer


class ExpenseListCreateAPIView(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExpenseDetailSerializer
        return super().get_serializer_class()

class ExpenseRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExpenseDetailSerializer
        return super().get_serializer_class()

# departmental expenses
class DepartmentalExpenses(ListAPIView):
    serializer_class = ExpenseDetailSerializer

    def get_queryset(self):
        departmental_expenses = Expense.objects.filter(budget__department__id=self.kwargs['department_id'])
        return departmental_expenses