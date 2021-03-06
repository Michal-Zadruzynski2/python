# Generated by Django 3.0.7 on 2020-06-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20200630_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie nr 1'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie nr 2'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie nr 3'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie nr 4'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie nr 5'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Pojemność'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(blank=True, max_length=32, verbose_name='Rodzaj paliwa'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.CharField(blank=True, max_length=32, verbose_name='Skrzynia biegów'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Zdjęcie główne'),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.PositiveSmallIntegerField(verbose_name='Moc'),
        ),
    ]
