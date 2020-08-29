from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_403_FORBIDDEN)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ...models import Tenant
from ..serializers.tenants import TenantSerializer


# retrieves a list of all tenants
class TenantListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


# retrieves an instance of a tenant, use this for login credentials
class TenantInfoAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request, **kwargs):
        data = request.data

        if 'tenant_id' in data.keys():
            tenant = get_object_or_404(Tenant, tenant_id=data['tenant_id'])

            if tenant.is_active:
                data = {
                    'name':tenant.name,
                    'subdomain': tenant.subdomain,
                    'organization_id': tenant.tenant_id
                }

                return Response(data, status=HTTP_200_OK)
            else:
                return Response(
                    {
                        'detail':
                        'It appears your organization is inactive, please contact support to rectify this.'
                    },
                    status=HTTP_403_FORBIDDEN)

        else:
            return Response(
                {'detail': 'Please pass tenant_id as a key in your request'},
                status=HTTP_400_BAD_REQUEST)
