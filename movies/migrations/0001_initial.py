# Generated by Django 3.0.8 on 2020-07-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=300)),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]