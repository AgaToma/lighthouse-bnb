# Generated by Django 3.2.19 on 2023-06-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]