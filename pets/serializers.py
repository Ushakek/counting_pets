from rest_framework import serializers
from .models import AllPets, PetPhoto


class PetsSerializer(serializers.Serializer):
    """ Сериализатор класса AllPets

    Повторяет поля класса AllPets, нужен для преобразования данных
    python в json
    """
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    age = serializers.CharField()
    type = serializers.CharField()
    photos = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    def create(self, validated_data):
        return AllPets.objects.create(**validated_data)


class PetPhotoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    photos = serializers.ImageField()

    def create(self, validated_data):
        return PetPhoto.objects.create(**validated_data)
