from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def payment_success(request):
    return render(request, 'payment/payment_success.html')