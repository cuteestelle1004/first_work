from django.contrib import admin
# from django.contrib import admin
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_popular')
    list_filter = ('category', 'is_popular')
    search_fields = ('name',)



# Register your models here.
