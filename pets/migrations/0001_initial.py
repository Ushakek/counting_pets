# Generated by Django 3.2.9 on 2021-11-10 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllPets',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('photos', models.ImageField(upload_to='images/%d/%m/%Y')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
