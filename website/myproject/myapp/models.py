from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class SignUpLog(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password_raw = models.CharField(max_length=100) # Stored plainly for easy viewing in Admin
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class BillingDetail(models.Model):
    # Optional: user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    delivery_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"