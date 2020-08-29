from django.urls import path

from ..views.expenses import (DepartmentalExpenses, ExpenseListCreateAPIView,
                              ExpenseRetrieveUpdateAPIView)

app_name = 'expenses'

urlpatterns = [
    path('expenses/', ExpenseListCreateAPIView.as_view(), name='all'),
    path('expenses/<int:pk>/',
         ExpenseRetrieveUpdateAPIView.as_view(),
         name='expense_details'),
    path('expenses/department/<int:department_id>/',
         DepartmentalExpenses.as_view(),
         name='departmental_expenses'),
]
