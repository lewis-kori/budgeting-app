from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from ...models import Department
from ..serializers.departments import DepartmentSerializer

# retrieves a list of all departments
class DepartmentListCreateAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer