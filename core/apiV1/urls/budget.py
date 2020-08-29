from django.urls import path

from ..views.budget import (BudgetListCreateAPIView,
                            BudgetRetrieveUpdateAPIView,
                            DepartmentalBudgetsListAPIView)

app_name = 'budgets'

urlpatterns = [
    path('budgets/', BudgetListCreateAPIView.as_view(), name='all'),
    path('budgets/<int:pk>/',
         BudgetRetrieveUpdateAPIView.as_view(),
         name='budget_details'),
    path('budgets/department/<int:department_id>/',
         DepartmentalBudgetsListAPIView.as_view(),
         name='departmental_budgets'),
]
