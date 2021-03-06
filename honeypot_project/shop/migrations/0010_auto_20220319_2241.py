# Generated by Django 3.2.12 on 2022-03-20 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20220305_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='default description', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='100 ETH', max_length=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
