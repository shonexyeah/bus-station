from django.urls import path
from routes.views import RouteList, RouteDetail

urlpatterns = [
    path('', RouteList.as_view(), name='route-list'),
    path('<int:pk>/', RouteDetail.as_view(), name='route-detail'),
]
