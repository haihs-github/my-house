# Generated by Django 4.2.7 on 2024-11-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myHouse', '0004_alter_congno_sodien_alter_congno_sonuoc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congno',
            name='phong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='congno', to='myHouse.phong'),
        ),
    ]
