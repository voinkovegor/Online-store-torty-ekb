from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Topping, Dekor
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def contacts(request):
    return render(request, 'shop/headers/contacts.html')

def toppings_and_decoration(request):
    toppings = Topping.objects.all()
    dekors = Dekor.objects.filter(available=True)
    return render(request,
                  'shop/headers/toppings_and_decoration.html',
                  {'toppings': toppings,
                   'dekors': dekors})

def tiered_cakes(request):
    return render(request, 'shop/headers/tiered_cakes.html')

def order_and_payment(request):
    return render(request, 'shop/headers/order_and_payment.html')