from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    calories = models.PositiveIntegerField()
    category = models.CharField(max_length=50, default='general')
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart ({self.user or self.session_key})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.food.name} x {self.quantity}"
