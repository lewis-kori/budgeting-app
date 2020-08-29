from django.urls import include,path

urlpatterns = [
    path('',include('tenants.apiV1.urls.tenants')),
    path('',include('tenants.apiV1.urls.departments')),
]
