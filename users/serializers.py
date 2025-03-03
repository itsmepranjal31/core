from rest_framework import serializers
from django.contrib.auth import get_user_model
from profiles.models import Profile  # ✅ Import Profile Model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    codeforces_username = serializers.CharField(required=True)  # ✅ Require Codeforces ID

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'codeforces_username']

    def create(self, validated_data):
        codeforces_username = validated_data.pop('codeforces_username')  # ✅ Extract Codeforces ID
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, codeforces_username=codeforces_username)  # ✅ Create Profile
        return user
