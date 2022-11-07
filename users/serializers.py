from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email',
                  'is_admin', 'bio', 'first_name', 'image']

    def get_is_admin(self, obj):
        return obj.is_staff
