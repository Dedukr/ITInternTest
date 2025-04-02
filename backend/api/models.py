from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user1 = models.CharField(max_length=255, blank=True, null=True)
    user2 = models.CharField(max_length=255, blank=True, null=True)
    user3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name