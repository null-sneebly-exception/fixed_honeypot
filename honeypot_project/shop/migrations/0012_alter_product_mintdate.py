# Generated by Django 3.2.12 on 2022-04-15 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20220319_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mintdate',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
