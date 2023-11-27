from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm

def index(request):
    return render(request, 'pages/index.html')


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


def products(request):
    return render(request, 'pages/products.html')
