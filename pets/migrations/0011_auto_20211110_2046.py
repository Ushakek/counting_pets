# Generated by Django 3.2.9 on 2021-11-10 20:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0010_alter_allpets_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photos', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='allpets',
            name='photos',
            field=models.JSONField(null=True),
        ),
    ]
