# Generated by Django 2.1 on 2019-03-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=264)),
                ('userName', models.CharField(max_length=264)),
                ('branch', models.CharField(max_length=264)),
                ('path', models.CharField(max_length=264)),
            ],
        ),
    ]
