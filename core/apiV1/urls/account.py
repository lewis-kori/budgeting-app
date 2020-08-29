from django.urls import path

from ..views.account import AccountListCreateAPIView, AccountRetrieveUpdateAPIView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', AccountListCreateAPIView.as_view(), name='all'),
    path('accounts/<int:pk>/',
         AccountRetrieveUpdateAPIView.as_view(),
         name='account_details'),
]
