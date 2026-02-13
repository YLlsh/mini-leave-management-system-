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