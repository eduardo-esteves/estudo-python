from django.shortcuts import render

# Create your views here.

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
