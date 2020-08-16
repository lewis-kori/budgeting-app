from rest_framework.generics import ListCreateAPIView

from ...models import Tenant
from ..serializers.tenants import TenantSerializer


class TenantListCreateAPIView(ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
