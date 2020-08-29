from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from ...models import Account
from ..serializers.account import AccountSerializer


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
