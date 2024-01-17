from django.db import models

# Create your models here.
class Waitlist(models.Model):
        name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        customer_type = models.CharField(max_length=255)
        date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"{self.name}  |   {self.customer_type}   |    {self.date}"
