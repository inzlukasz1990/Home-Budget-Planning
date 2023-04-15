from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'location']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], bio=validated_data['bio'], location=validated_data['location'])
        return user

