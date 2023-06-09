# Generated by Django 4.2 on 2023-04-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Delete (deactivate) the current image'),
        ),
    ]
