from django.urls import path
from .views import payment_success,  checkout, billing_info

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path("payment_success/", payment_success, name="payment_success"),
    path("billing_info",billing_info, name='billing_info')
]
