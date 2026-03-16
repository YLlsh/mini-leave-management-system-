import random
import string
from django.shortcuts import render, redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import response
from .serializer import CustomeSerializer
from rest_framework.decorators import api_view, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from .models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CustomeLoginView(TokenObtainPairView):
    serializer_class = CustomeSerializer


class add_leave_viewset(ModelViewSet):
    queryset = leave_requests.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get_queryset(self):
        if self.request.user.groups.filter(name="manager").exists():
            return super().get_queryset()
        else:
            return leave_requests.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class Ismanager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="manager").exists()


class modify_leave_status(ModelViewSet):
    queryset = leave_requests.objects.all()
    serializer_class = LeaveSerializer
    http_method_names = ["patch"]
    permission_classes = [IsAuthenticated, Ismanager]


def genearate(name):

    name = name.split(' ')[0]
    d = string.digits

    d = ''.join(random.choices(d, k=4))
    username = name+d

    return username


class EmployeeView(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        name = self.request.data.get('name')

        username = password = genearate(name)
        print(username)
        user = User(username=username)
        user.set_password(password)
        user.save()

        return serializer.save(user=user)

    def perform_destroy(self, instance):

        user = instance.user
        user.delete()

        return super().perform_destroy(instance)


def get_emp_id(request, id):
    return redirect(f"/add_employee?emp_id={id}")



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_employee(request):

    emp_id = request.data.get("emp_id")

    emp = Employee.objects.get(emp_id=emp_id)

    return Response({
        "name": emp.name,
        "age": emp.age,
        "position": emp.position,
        "salary": emp.salary
    })



