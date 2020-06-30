from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year','engine', 'fuel', 'power',
                  'gearbox', 'description', 'mileage', 'photo',
                  'photo1']

