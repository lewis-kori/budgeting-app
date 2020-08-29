from django.urls import path

from ..views.tenants import TenantInfoAPIView, TenantListCreateAPIView

app_name='tenants'

urlpatterns = [
    path('tenants/', TenantListCreateAPIView.as_view(),name='tenants'),
    path('tenants/info/', TenantInfoAPIView.as_view(),name='tenant_info'),
]
