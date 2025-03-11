from django.urls import path
from .views import attendance_list,homepage

urlpatterns=[
    path('',homepage,name='homepage'),
    #path('attendance/',attendance_list,name='attendance_list'),
]