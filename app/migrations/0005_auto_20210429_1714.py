# Generated by Django 3.1.7 on 2021-04-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_healthyheart_users_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthyheart_users',
            name='Result',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
