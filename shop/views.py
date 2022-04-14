from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None, params=None):
    category = None
    categories = Category.objects.all()
    value = request.GET.get('search')
    if value:
        products = Product.objects.filter(name__contains=value).filter(available=True)
    else: products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'value': value})


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



def about(request):
    return render(request, 'shop/headerpage/about.html')



def delivery(request):
    return render(request, 'shop/headerpage/deliver.html')


def back(request):
    return render(request, 'shop/headerpage/back.html')

def garant(request):
    return render(request, 'shop/headerpage/garant.html')
