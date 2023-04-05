# Generated by Django 4.2 on 2023-04-05 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Activate/Deactivate the current gallery'),
        ),
        migrations.AddField(
            model_name='image',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Deleted (deactivate) the current image'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]