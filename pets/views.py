from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllPets
from .serializers import PetsSerializer


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
