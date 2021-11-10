from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllPets
from .serializers import PetsSerializer


class CreateView(APIView):
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
