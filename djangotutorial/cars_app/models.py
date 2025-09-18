from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)         # e.g. Toyota
    model = models.CharField(max_length=100)        # e.g. Corolla
    year = models.PositiveIntegerField(max_length=100)
    price = models.FloatField(max_length=50)
    description = models.TextField(default="strong and reliable car for everyday use")
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

# Create your models here.
