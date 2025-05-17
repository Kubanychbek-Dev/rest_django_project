from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as gtl


class UserRoles(models.TextChoices):
    ADMIN = "admin", gtl("admin")
    MODERATOR = "moderator", gtl("moderator")
    MEMBER = "member", gtl("member")


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=gtl("Email"))
    role = models.CharField(max_length=14, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name=gtl  ("Role"))
    first_name = models.CharField(max_length=40, verbose_name=gtl("First Name"), blank=True, null=True)
    last_name = models.CharField(max_length=40, verbose_name=gtl("Last Name"), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=gtl("Phone number"), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=gtl("Is active"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = gtl("User")
        verbose_name_plural = gtl("Users")
        ordering = ["id"]