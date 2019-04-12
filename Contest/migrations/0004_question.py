# Generated by Django 2.1 on 2019-03-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0003_auto_20190329_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('questionID', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=264)),
                ('answer', models.CharField(max_length=264)),
                ('contestID', models.ManyToManyField(to='Contest.contest')),
            ],
        ),
    ]
