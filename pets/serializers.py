from rest_framework import serializers
from .models import AllPets


class PetsSerializer(serializers.Serializer):
    """ Сериализатор класса AllPets

    Повторяет поля класса AllPets, нужен для преобразования данных
    python в json
    """
    id = serializers.CharField(default=None)
    name = serializers.CharField(max_length=50)
    age = serializers.CharField()
    type = serializers.CharField()
    # photos = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    def create(self, validated_data):
        return AllPets.objects.create(**validated_data)
