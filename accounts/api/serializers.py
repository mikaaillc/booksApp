from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('pk','email','password')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('pk','email','password')


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_data(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Giriş Başarısız")

