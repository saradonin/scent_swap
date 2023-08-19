# Generated by Django 4.2.4 on 2023-08-15 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scent_app', '0003_remove_perfume_category_alter_brand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swapoffer',
            name='message',
        ),
        migrations.AlterField(
            model_name='userperfume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='perfume',
            unique_together={('name', 'brand', 'concentration')},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
