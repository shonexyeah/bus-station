from django.urls import path
from vehicles.views import BusList, BusDetail

urlpatterns = [
    path('', BusList.as_view(), name='bus-list'),
    path('<int:pk>/', BusDetail.as_view(), name='bus-detail'),
    #path('<int:pk>/', BusDelete.as_view(), name='bus-delete'),
]