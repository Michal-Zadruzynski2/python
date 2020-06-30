# Generated by Django 3.0.7 on 2020-06-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20200630_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='gearbox',
            field=models.CharField(blank=True, default='a', max_length=32, verbose_name='Skrzynia biegów'),
        ),
        migrations.AddField(
            model_name='car',
            name='power',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Moc'),
        ),
    ]