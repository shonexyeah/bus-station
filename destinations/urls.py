from django.urls import path
from destinations.views import DestinationListCreate, DestinationDetail



urlpatterns = [
    path('', DestinationListCreate.as_view(), name='destination-list-create'),
    path('<int:pk>/', DestinationDetail.as_view(), name='destination-detail'),

]