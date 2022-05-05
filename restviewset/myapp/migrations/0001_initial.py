# Generated by Django 3.1.13 on 2022-04-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('roll', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
