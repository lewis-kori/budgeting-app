from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from ...models import Expense
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
