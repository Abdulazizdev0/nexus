from rest_framework import serializers
from user.models import User,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('firstname','last_name','phone_number',)
        read_only_fields = ('user',)