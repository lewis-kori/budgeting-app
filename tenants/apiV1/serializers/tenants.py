from rest_framework.serializers import ModelSerializer

from ...models import Tenant


class TenantSerializer(ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'
