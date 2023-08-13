# Generated by Django 4.2.4 on 2023-08-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scent_app', '0002_perfume_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='category',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]