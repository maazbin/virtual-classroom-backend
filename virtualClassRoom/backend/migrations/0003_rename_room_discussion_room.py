# Generated by Django 3.2.9 on 2022-01-06 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_discussion_room_discussion_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='Room',
            new_name='room',
        ),
    ]
