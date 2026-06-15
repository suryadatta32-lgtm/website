from django.contrib import admin
from .models import ContactMessage, SignUpLog
from .models import BillingDetail

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')

@admin.register(SignUpLog)
class SignUpLogAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'registered_at')
# Register your models here.

@admin.register(BillingDetail)
class BillingDetailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'country', 'delivery_type', 'created_at')