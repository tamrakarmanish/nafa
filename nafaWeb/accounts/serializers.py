from django import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "password", "email", "first_name", "last_name")