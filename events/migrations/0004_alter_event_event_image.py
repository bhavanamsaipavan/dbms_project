# Generated by Django 4.2.6 on 2023-10-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default='default_image.jpg', upload_to='media/event_images/'),
        ),
    ]
