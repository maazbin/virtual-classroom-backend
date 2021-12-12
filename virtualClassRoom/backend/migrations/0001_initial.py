# Generated by Django 3.2.9 on 2021-12-11 19:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=122, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
    ]
