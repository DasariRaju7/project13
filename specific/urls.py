from specific.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('raju/',raju,name='raju'),
    path('ravi/',ravi,name='ravi'),
]