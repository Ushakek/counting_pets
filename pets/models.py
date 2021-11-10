import uuid

from django.db import models
from rest_framework import fields


class AllPets(models.Model):
    """ Модель для записи в базу данных

    fields:
        id(uuid): Поле с автоматической генерацией UUID4, является pk
        name(Char): Поле для записи имени питомца, максимальная длинна 100
        age(Float): Поле для записи возраста питомца, по умолчанию равно нулю
        type(Char): Вид питомца (кошка, собака, корова), максимальная длинна 50
        created_at: дата и время введение в систему питомца. Создаётся автоматически
    """
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=100)
    age = models.FloatField(default=0)
    type = models.CharField(max_length=50)
    # photos = models.FilePathField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class PetPhoto:
#     """ Модель создания фотографий
#
#     photos(Image): Фотографии питомца
#     """
#     photos = models.ImageField(null=True, upload_to=f'images_{uuid.uuid4()}')
