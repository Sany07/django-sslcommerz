
from django.urls import path
from .views import *


app_name = "donationapp"

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('donate/', DonateView, name='donate'),
    path('success/', CheckoutSuccessView.as_view(), name='success'),
    path('faild/', CheckoutFaildView.as_view(), name='faild'),

]
