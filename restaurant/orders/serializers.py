from rest_framework import serializers
from database.models import Dishes


class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ('id', 'name', 'image', 'description', 'price')

    def create(self, validated_data):
        return Dishes.objects.create(**validated_data)