# Generated by Django 3.2.5 on 2022-02-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='helloLuckNum',
            field=models.IntegerField(default=0),
        ),
    ]
