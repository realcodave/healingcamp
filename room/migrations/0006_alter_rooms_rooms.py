# Generated by Django 4.0.2 on 2022-02-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_rooms_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]