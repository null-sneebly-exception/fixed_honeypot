# Generated by Django 3.2.12 on 2022-03-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20220319_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mintdate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='100 ETH', max_length=20),
        ),
    ]
