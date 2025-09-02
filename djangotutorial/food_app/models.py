from django.db import models

# Create your models here.
# A WEBSITE WHERE USERS CAN ORDER FOOD
class Food(models.Model):
    price= models.FloatField(max_length=60,editable=False)
    description= models.TextField(max_length=500)
    images= models.ImageField()
    name= models.CharField(max_length=500)