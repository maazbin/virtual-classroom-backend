# Generated by Django 3.2.9 on 2022-01-06 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_topic_discussion_topic_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='discussion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.discussion'),
        ),
    ]