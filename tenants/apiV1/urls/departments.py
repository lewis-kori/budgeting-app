from django.urls import path

from ..views.departments import DepartmentRetrieveUpdateView, DepartmentListCreateAPIView

app_name='departments'

urlpatterns = [
    path('departments/', DepartmentListCreateAPIView.as_view(),name='departments'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateView.as_view(),name='departments_info'),
]
