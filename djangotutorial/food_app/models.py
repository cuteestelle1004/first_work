from django.db import models

# Create your models here.
# A WEBSITE WHERE USERS CAN ORDER FOOD
# class Food(models.Model):

#     name= models.CharField(max_length=500)
#     price= models.FloatField(max_length=60)
#     description= models.TextField(max_length=500)
#     images= models.ImageField()
#     calories = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name


class Food(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()  # max_length is not valid for FloatField
    description = models.TextField(max_length=500)
    images = models.ImageField(null=True, blank=True)
    calories = models.PositiveIntegerField()
    category = models.CharField(max_length=50, default='general')  # ✅ New field



    def __str__(self):
        return self.name
