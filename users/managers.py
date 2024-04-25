from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create user logic here
        pass

    def create_superuser(self, email, password=None, **extra_fields):
        # Create superuser logic here
        pass
