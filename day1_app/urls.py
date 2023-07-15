from django.urls import path
from day1_app.views import *

urlpatterns = [
    path('Friend_detail/<int:pk>/', Friend_detail, name='Friend_detail'),
    path('Friend_list/', Friend_list, name='Friend_list'),
]