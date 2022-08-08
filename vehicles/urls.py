from django.urls import path
from vehicles.views import VehicleListCreate, VehicleDetail


urlpatterns = [
    path('', VehicleListCreate.as_view(), name='vehicle-list-create'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
]