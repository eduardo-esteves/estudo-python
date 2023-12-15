from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from fusion.models import Services, Team_Members
from fusion.forms import ContactForm

# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['employees'] = Team_Members.objects.order_by('?').all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form)
