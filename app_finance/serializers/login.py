from rest_framework import serializers


# Author Nithin
class LoginSerializer(serializers.Serializer):
    """Serializer to get the inputs from login user"""

    username = serializers.CharField()
    password = serializers.CharField()



