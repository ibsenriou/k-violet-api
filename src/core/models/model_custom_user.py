import typing
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import QuerySet



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers

    The create_user and create_superuser methods are required to work with the Django admin app
    This is because the Django admin app expects a username field to be present on the User model
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def add_points(self, user: "CustomUser", points: int) -> "CustomUser":
        user.coins += points
        user.amassed_coins += points
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model

    This is a custom user model that uses email as the unique identifier for authentication instead of usernames.
    """
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    coins = models.IntegerField(default=0)
    amassed_coins = models.IntegerField(default=0)


    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
