from django.core.exceptions import ValidationError, ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllPets, PetPhoto
from .serializers import PetsSerializer, PetPhotoSerializer


class CreateView(APIView):
    """ Класс представлений модели AllPets

    Нужен для взаимодействия с моделями данных. Реализован на APIView.
    Methods:
        get: Получение всех данных из базы
        post: Добавление в базу новых данных
    """
    def get(self, request):
        limit = request.data.get('limit', 20)
        limit = round(limit)
        # todo: Исключить поле, offset?
        hash_photos = request.data.get('hash_photos', None)
        pets = AllPets.objects.all()[:limit]
        serializer = PetsSerializer(pets, many=True)

        return Response({
            'count': len(serializer.data),
            'items': [serializer.data],
        })

    def post(self, request):
        pet = request.data.get('pet')

        serializer = PetsSerializer(data=pet)
        if serializer.is_valid(raise_exception=True):
            pet_save = serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        pets = request.data.get('ids')
        pool_err = []
        for idx, id_pet in enumerate(pets, start=1):
            pet = AllPets.objects.get(pk=id_pet)
            try:
                pet.delete()
            # todo: Не перехватывает ошибку
            except AllPets.DoesNotExist:
                pool_err.append({'id': str(id_pet),
                                 'error': 'Pet with matching ID was not found'})
            id_photo = pet.photos
            if len(id_photo) > 0:
                id_photo = id_photo[0].get('id')
                photo = PetPhoto.objects.get(pk=id_photo)
                photo.delete()
                photo.photos.delete()

            count = idx - len(pool_err)
        return Response({'deleted': count,
                         'errors': pool_err})


class PostPhotosView(APIView):
    """ Класс представления модели PetPhoto

    Нужен для загрузки фотографий к определённому питомцу. Реализован на APIView.
    Methods:
        post: принимает pk(id(для модели данных в AllPets) или uid(должен быть)) из строки,
        который должен быть привязан к определённому питомцу.
    """
    def post(self, request, pk):
        try:
            data = AllPets.objects.get(pk=pk)
        except ValidationError as error:
            return Response({'message': {
                             'error': error}})
        file = request.data
        image_serializer = PetPhotoSerializer(data=file)

        if image_serializer.is_valid(raise_exception=True):
            image_serializer.save()
            data.photos = [{'id': str(image_serializer.data.get('id')),
                            'url': image_serializer.data.get('photos')}]
            data.save()
        return Response(image_serializer.data)
