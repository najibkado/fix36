from django.shortcuts import render
from django.http import HttpResponse
from .models import Waitlist

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'main/contact.html')
    
    if request.method == 'POST':
        
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        customer_type = request.POST['customer_type']

        if int(customer_type) == 1:
            customer_type = "End User"
        elif int(customer_type) == 2:
            customer_type = "Service Provider"
        else:
            customer_type = "Both"

        customer = Waitlist(
            name = name,
            phone = phone,
            email = email,
            customer_type = customer_type 
        )

        customer.save()

        return HttpResponse("Successfull!")



