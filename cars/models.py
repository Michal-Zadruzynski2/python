from django.db import models


class Car(models.Model):
    make = models.CharField(verbose_name="Marka", max_length=32, blank=False)
    model = models.CharField(max_length=32, blank=False)
    year = models.PositiveSmallIntegerField(verbose_name="Rok produkcji", blank=False)
    engine = models.PositiveSmallIntegerField(verbose_name="Pojemność", blank=True)
    fuel = models.CharField(verbose_name="Rodzaj paliwa", max_length=32, blank=True)
    power = models.PositiveSmallIntegerField(verbose_name="Moc", blank=False)
    gearbox = models.CharField(verbose_name="Skrzynia biegów", max_length=32, blank=True)
    description = models.TextField(verbose_name="Opis", blank=True)
    mileage = models.PositiveIntegerField(verbose_name="Przebieg (w km)", blank=False)
    photo = models.ImageField(verbose_name="Zdjęcie główne", upload_to='photos', null=True, blank=True)
    photo1 = models.ImageField(verbose_name="Zdjęcie nr 1", upload_to='photos', null=True, blank=True)



    def __str__(self):
        return self.make + ' ' + self.model
