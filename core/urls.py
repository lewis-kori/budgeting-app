from django.urls import path, include

urlpatterns = [
    path('',include('core.apiV1.urls.account')),
    path('',include('core.apiV1.urls.budget')),
    path('',include('core.apiV1.urls.expenses')),
]
