# Generated by Django 4.2.7 on 2024-11-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHouse', '0005_alter_congno_phong'),
    ]

    operations = [
        migrations.AddField(
            model_name='congno',
            name='tienphong',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='phong',
            name='tienphong',
            field=models.FloatField(default=0),
        ),
    ]
