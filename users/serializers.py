from rest_framework import serializers
from users.models import User


class UserSerializaer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ip']
