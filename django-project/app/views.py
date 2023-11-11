from django.shortcuts import render

from app.models import Product


def index(request):
    context = {
        'title': 'Home - Django Framework',
        'h1': 'Welcomme to the Django Framework',
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'title': 'Contato - Django Framework',
        'h1': 'Contact',
    }
    return render(request, 'contact.html', context)

def product(request, id):
    product = Product.objects.get(id=id)

    context = {
        'title': f'{product.name} - Django Framework',
        'h1': 'Produto',
        'product': product,
    }

    return render(request, 'product.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'title': 'Produtos - Django Framework',
        'h1': 'Produtos',
        'products': products
    }

    return render(request, 'products.html', context)
