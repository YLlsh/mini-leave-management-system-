from django.shortcuts import render, redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import response
from .serializer import CustomeSerializer
from rest_framework.decorators import api_view
from .serializer import LeaveSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import leave_requests
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CustomeLoginView(TokenObtainPairView):
    serializer_class = CustomeSerializer


class add_leave_viewset(ModelViewSet):
    queryset = leave_requests.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post','get']

    def get_queryset(self):
        if self.request.user.groups.filter(name="manager").exists():
            return super().get_queryset()
        else:
            return leave_requests.objects.filter(user_id = self.request.user)
    
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
