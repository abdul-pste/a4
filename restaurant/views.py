from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'restaurant/main.html')

def order(request):
    return render(request, 'restaurant/order.html')

def confirmation(request):
    return render(request, 'restaurant/confirmation.html')

def submit_order(request):
    # Your order submission logic
    return render(request, 'restaurant/confirmation.html')