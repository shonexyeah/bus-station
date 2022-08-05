from django.urls import path
from vehicles.views import VehicleList, VehicleDetail


urlpatterns = [
    path('', VehicleList.as_view(), name='vehicle-list'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
]