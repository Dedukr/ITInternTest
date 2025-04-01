from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name