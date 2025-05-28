from django.utils.translation import gettext_lazy as gtl
from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsModerator(BasePermission):
  message = gtl("You are not a moderator")

  def has_permission(self, request, view):
    if request.user.is_authenticated and request.user.role == UserRoles.MODERATOR:
      return True
    return False


class IsSuperUser(BasePermission):
  message = gtl("You are not a superuser")

  def has_permission(self, request, view):
    if request.user.is_authenticated and request.user.is_superuser:
      return True
    return False