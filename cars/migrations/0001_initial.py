# Generated by Django 3.0.7 on 2020-06-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('year', models.PositiveSmallIntegerField()),
                ('mileage', models.PositiveIntegerField()),
            ],
        ),
    ]
