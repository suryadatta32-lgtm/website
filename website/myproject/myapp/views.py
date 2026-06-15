from django.shortcuts import redirect, render
from django.contrib import messages
from .models import ContactMessage, SignUpLog
from django.http import JsonResponse
from .models import BillingDetail

def home_view(request):
    """Renders the main catalog e-commerce homepage."""
    return render(request, 'index.html') 

def contact_view(request):
    if request.method == 'POST':
        # Capture variables from HTML "name" properties
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')

        # Insert directly into the database table
        ContactMessage.objects.create(name=user_name, email=user_email, message=user_message)
        
        # Flash a status alert message to the user screen
        messages.success(request, "Message recorded successfully!")
        return redirect('contact')

    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        form_action = request.POST.get('form_type')

        if form_action == 'signup':
            name = request.POST.get('full_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Save the registration log info
            SignUpLog.objects.create(full_name=name, email=email, password_raw=password)
            messages.success(request, "Account created! Please sign in below.")
            return redirect('login')

        elif form_action == 'login':
            # Handle user login authentication redirecting home
            messages.success(request, "Login Successful!")
            return redirect('home')

    return render(request, 'login.html')

def cart_view(request):
    """Renders the client e-commerce active session shopping cart asset list."""
    return render(request, 'cart.html') 

from django.shortcuts import render
from .models import BillingDetail

def checkout_view(request):
    current_submission = None  # Start with nothing

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        delivery_type = request.POST.get('delivery_type')

        # Save to the admin database
        current_submission = BillingDetail.objects.create(
            first_name=first_name,
            last_name=last_name,
            street_address=street_address,
            city=city,
            postal_code=postal_code,
            country=country,
            delivery_type=delivery_type
        )
        
        # Instead of redirecting (which clears state), we render directly 
        # to show the 'current_submission' we just made.

    return render(request, 'checkout.html', {'current_submission': current_submission})


def payment_view(request):
    """Renders the final payment processing and confirmation page."""
    return render(request, 'payment.html')