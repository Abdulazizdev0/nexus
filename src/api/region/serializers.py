from rest_framework import serializers

from category.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region

        fields = '__all__'