from django.urls import path
from . import views

urlpatterns = [
    # 🔹 Main Pages
    path('', views.home, name='home'),
    path('popular/', views.popular_dishes, name='popular'),
    path('rice/', views.rice_dishes, name='rice'),
    path('pasta/', views.pasta_dishes, name='pasta'),
    path('grilled/', views.grilled_items, name='grilled'),

    # 🛒 Cart System
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:food_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]
