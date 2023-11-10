from django.shortcuts import render

from app.models import Product


def index(request):
    context = {
        'title': 'Home - Django Framework',
        'h1': 'Bem vindo a pagina Django Framework'
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'title': 'Contato - Django Framework',
        'h1': 'Contato'
    }
    return render(request, 'contact.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'title': 'Produtos - Django Framework',
        'h1': 'Produtos',
        'products': products
    }

    return render(request, 'products.html', context)
