# Generated by Django 4.2.7 on 2024-11-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHouse', '0006_congno_tienphong_phong_tienphong'),
    ]

    operations = [
        migrations.AddField(
            model_name='phong',
            name='stt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='phong',
            name='vitri',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
