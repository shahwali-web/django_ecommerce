from django.urls import path
from .views import payment_success  # Import the view

urlpatterns = [
    path("payment_success/", payment_success, name="payment_success"),
]
