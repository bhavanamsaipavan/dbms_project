# Generated by Django 4.2.6 on 2023-10-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default='default_image.webp', upload_to='event_images/'),
        ),
    ]
