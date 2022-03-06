# Generated by Django 4.0 on 2022-03-06 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='response_topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.topic'),
        ),
        migrations.AddField(
            model_name='response',
            name='response_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.user'),
        ),
    ]
