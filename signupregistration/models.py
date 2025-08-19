from django.db import models
from django.core.exceptions import ValidationError

class SignUpRegistration(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default="")

    def clean(self):
        """Model-level validation"""
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")

        if not self.first_name or not self.last_name or not self.email or not self.username:
            raise ValidationError("All required fields must be filled.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
