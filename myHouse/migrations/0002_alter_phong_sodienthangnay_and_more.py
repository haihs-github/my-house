# Generated by Django 4.2.7 on 2024-09-19 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phong',
            name='sodienthangnay',
            field=models.BigIntegerField(default=models.BigIntegerField(default=0)),
        ),
        migrations.AlterField(
            model_name='phong',
            name='sonuocthangnay',
            field=models.BigIntegerField(default=models.BigIntegerField(default=0)),
        ),
    ]
