# Generated by Django 2.2.14 on 2020-07-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.CharField(max_length=100),
        ),
    ]
