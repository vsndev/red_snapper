# Generated by Django 2.2 on 2019-04-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red_snapper_app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
