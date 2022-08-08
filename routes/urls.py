from django.urls import path
from routes.views import RouteListCreate, RouteDetail

urlpatterns = [
    path('', RouteListCreate.as_view(), name='route-list-create'),
    path('<int:pk>/', RouteDetail.as_view(), name='route-detail'),

]
