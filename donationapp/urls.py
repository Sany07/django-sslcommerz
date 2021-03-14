
from django.urls import path
from .views import *


app_name = "newspaper"

urlpatterns = [

    path('', IndexView, name='home'),
]
