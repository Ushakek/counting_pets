# Generated by Django 3.2.9 on 2021-11-11 15:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0013_auto_20211110_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpets',
            name='photos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
    ]