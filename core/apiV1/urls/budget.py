from django.urls import path

from ..views.budget import BudgetListCreateAPIView, BudgetRetrieveUpdateAPIView

app_name = 'budgets'

urlpatterns = [
    path('budgets/', BudgetListCreateAPIView.as_view(), name='all'),
    path('budgets/<int:pk>/',
         BudgetRetrieveUpdateAPIView.as_view(),
         name='budget_details'),
]
