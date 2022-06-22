from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Product, Category


def home_page(request):
    categories = Category.objects.all()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    context = {
        'categories': categories,
        'cart': cart,
    }
    return render(request, template_name='shop/home_page.html', context=context)


def get_category(request, category_id):
    product = Product.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, id=category_id)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    context ={
        'category': category,
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart,
    }
    return render(request, 'shop/category.html', context=context)


# def product_detail(request, product_id):
