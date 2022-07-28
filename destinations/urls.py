from django.urls import path
from destinations.views import DestinationList, DestinationDetail

urlpatterns = [
    path('', DestinationList.as_view(), name='deastination-list'),
    path('<int:pk>/', DestinationDetail.as_view(), name='destination-detail'),

]