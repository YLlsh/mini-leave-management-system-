from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import leave_requests

class CustomeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data =  super().validate(attrs)

        user = self.user
        data["username"] = user.username
        if user.groups.filter(name="manager").exists():
            data["role"] = "manager"
            
        else:
            data["role"] = "user"

        return data
    

class LeaveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user_id.username", read_only=True)

    class Meta:
        model = leave_requests
        fields = ['id', 'leave_type', 'start_data', 'end_date', 'reason', 'status','remark','user_id', 'username']
        read_only_fields = ['user_id']


        
    def validate(self, data):
        start_date = data.get("start_data")
        end_date = data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise serializers.ValidationError(
                    {"end_date": "End date cannot be earlier than start date."}
                )

        return data
