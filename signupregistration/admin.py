from django.contrib import admin
from .models import SignUpRegistration

@admin.register(SignUpRegistration)
class SignUpRegistrationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "username", "gender", "date_registered")
    search_fields = ("first_name", "last_name", "email", "username")
    list_filter = ("gender", "date_registered")
