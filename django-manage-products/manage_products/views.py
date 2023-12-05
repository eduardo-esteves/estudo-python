from django.shortcuts import render, redirect
from django.contrib import messages

from manage_products.forms import ContactForm, ProductModelForm
from manage_products.models import Product

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Enviado com sucesso!')
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')

    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context)


def product(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao salvar produto')
        form = ProductModelForm()
        context = {
            'form': form
        }
        return render(request, 'pages/product.html', context)
    else:
        return redirect('index')
