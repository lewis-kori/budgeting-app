from django.urls import path

from ..views.tenants import TenantListCreateAPIView

app_name='tenants'

urlpatterns = [
    path('tenants/', TenantListCreateAPIView.as_view(),name='tenants'),
]
