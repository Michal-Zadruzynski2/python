from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required

def cars(request):
    all = Car.objects.all
    return render(request, 'cars.html', {'cars': all})

@login_required()
def new_car(request):
    form = CarForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(cars)

    return render(request, 'car form.html', {'form': form})

@login_required()
def edit_car(request, id):
    car = get_object_or_404(Car, pk=id)
    form = CarForm(request.POST or None, request.FILES or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect(cars)

    return render(request, 'car form.html', {'form': form})

@login_required()
def delete_car(request, id):
    car = get_object_or_404(Car, pk=id)
    form = CarForm(request.POST or None, request.FILES or None, instance=car)

    if request.method == "POST":
        car.delete()
        return redirect(cars)

    return render(request, 'submit.html', {'form': form})

def car_offer(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'car offer.html', {'car': car})
