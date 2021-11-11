from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllPets
from .serializers import PetsSerializer, PetPhotoSerializer


class CreateView(APIView):
    """ Класс представлений модели AllPets

    Нужен для взаимодействия с моделями данных. Реализован на APIView.
    Methods:
        get: Получение всех данных из базы
        post: Добавление в базу новых данных
    """
    def get(self, request):
        pets = AllPets.objects.all()
        serializer = PetsSerializer(pets, many=True)

        return Response({
            "count": len(serializer.data),
            "items": [serializer.data],
        })

    def post(self, request):
        pet = request.data.get('pet')

        serializer = PetsSerializer(data=pet)
        if serializer.is_valid(raise_exception=True):
            pet_save = serializer.save()
        return Response(serializer.data)


class PostPhotosView(APIView):
    def post(self, request, pk):
        try:
            data = AllPets.objects.get(pk=pk)
        except ValidationError as error:
            return Response({'message': {
                             'error': error}})
        file = request.data
        print(request.data['photos'])
        image_serializer = PetPhotoSerializer(data=file)
        if image_serializer.is_valid(raise_exception=True):
            image_serializer.save()
            data.photos = [{'id': str(image_serializer.data.get('id')),
                            'url': image_serializer.data.get('photos')}]
            data.save()
        return Response(image_serializer.data)
