from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Food, Cart, CartItem


# 🔹 Helper: get or create a cart for the user/session
def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


# 🔹 Home Page View
def home(request):
    foods = Food.objects.all()

    # Count for each category
    popular_count = Food.objects.filter(category__iexact='popular').count()
    rice_count = Food.objects.filter(category__iexact='rice').count()
    pasta_count = Food.objects.filter(category__iexact='pasta').count()
    grilled_count = Food.objects.filter(category__iexact='grilled').count()

    cart = get_or_create_cart(request)
    cart_count = CartItem.objects.filter(cart=cart).count()

    context = {
        'foods': foods,
        'popular_count': popular_count,
        'rice_count': rice_count,
        'pasta_count': pasta_count,
        'grilled_count': grilled_count,
        'cart_count': cart_count,
    }
    return render(request, 'home.html', context)


# 🔹 Category Pages
def popular_dishes(request):
    foods = Food.objects.filter(category__iexact='popular')
    return render(request, 'category_page.html', {'foods': foods, 'title': 'Popular Dishes'})


def rice_dishes(request):
    foods = Food.objects.filter(category__iexact='rice')
    return render(request, 'category_page.html', {'foods': foods, 'title': 'Rice Dishes'})


def pasta_dishes(request):
    foods = Food.objects.filter(category__iexact='pasta')
    return render(request, 'category_page.html', {'foods': foods, 'title': 'Pasta Dishes'})


def grilled_items(request):
    foods = Food.objects.filter(category__iexact='grilled')
    return render(request, 'category_page.html', {'foods': foods, 'title': 'Grilled Dishes'})


# 🛒 CART MANAGEMENT
def view_cart(request):
    cart = get_or_create_cart(request)
    try:
        items = cart.items.select_related('food')
    except AttributeError:
        items = cart.cartitem_set.select_related('food')

    # Compute totals
    for item in items:
        item.total_price = item.food.price * item.quantity  # 🔹 Add this line

    total_price = sum(item.total_price for item in items)
    total_quantity = sum(item.quantity for item in items)

    context = {
        'cart': cart,
        'items': items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart = get_or_create_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


def remove_from_cart(request, food_id):
    cart = get_or_create_cart(request)
    cart_item = CartItem.objects.filter(cart=cart, food_id=food_id).first()
    if cart_item:
        cart_item.delete()

    return redirect('view_cart')


def clear_cart(request):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(cart=cart).delete()
    return redirect('view_cart')
