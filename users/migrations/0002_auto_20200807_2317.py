# Generated by Django 3.0.7 on 2020-08-07 16:17

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=users.models.Profile.userDirectory),
        ),
    ]
