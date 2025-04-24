from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    class Meta:
        model = Blog
        fields = '__all__'
