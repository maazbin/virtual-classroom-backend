# Generated by Django 4.0 on 2022-03-07 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_comment_comment_response_comment_comment_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='Responses',
        ),
    ]
