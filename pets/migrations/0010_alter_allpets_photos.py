# Generated by Django 3.2.9 on 2021-11-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_alter_allpets_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpets',
            name='photos',
            field=models.FilePathField(null=True),
        ),
    ]
