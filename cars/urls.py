from django.urls import path
from cars.views import cars, new_car, edit_car, delete_car, car_offer

urlpatterns = [
    path('', cars, name='cars'),
    path('new-car/', new_car, name='new_car'),
    path('edit-car/<int:id>/', edit_car, name='edit_car'),
    path('delete-car/<int:id>/', delete_car, name='delete_car'),
    path('car-offer/<int:id>/', car_offer, name='car_offer')
]
