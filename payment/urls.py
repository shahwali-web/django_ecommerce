from django.urls import path
from .views import payment_success,  checkout

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path("payment_success/", payment_success, name="payment_success"),
]
