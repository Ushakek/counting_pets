from rest_framework import serializers
from .models import AllPets


class PetsSerializer(serializers.Serializer):
    id = serializers.CharField(default=None)
    name = serializers.CharField(max_length=50)
    age = serializers.CharField()
    type = serializers.CharField()
    # photos = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    def create(self, validated_data):
        print(validated_data['id'])
        validated_data['age'] = float(validated_data['age'])
        return AllPets.objects.create(**validated_data)

    # def
