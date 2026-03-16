from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class leave_requests(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=60,default=None)
    start_data = models.DateField(default=None)
    end_date = models.DateField(default=None)
    reason = models.TextField()
    status = models.CharField(default="pending")
    remark = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f"{self.user_id}"

class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    age = models.IntegerField(default=None)
    position = models.CharField(max_length=100, default=None)
    salary = models.IntegerField(default=None)
    join_date = models.DateField(auto_now_add=True)
    terminate_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'