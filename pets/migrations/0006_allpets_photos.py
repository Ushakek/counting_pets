# Generated by Django 3.2.9 on 2021-11-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20211110_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpets',
            name='photos',
            field=models.ImageField(default=[], upload_to='images\\%d\\%m\\%Y'),
        ),
    ]