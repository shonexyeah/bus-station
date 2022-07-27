from django.urls import path
from vehicles.views import BusList, BusDetail

urlpatterns = [
    path('', BusList.as_view(), name='bus-list'),
    path('add/', BusDetail.as_view(), name='bus-detail'),
]