
from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class User(AbstractUser):
    organization = models.ForeignKey(
        Organization, related_name="users", on_delete=models.CASCADE, null=True, blank=True
    )
    is_org_admin = models.BooleanField(default=False)
