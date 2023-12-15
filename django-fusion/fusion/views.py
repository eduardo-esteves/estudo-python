from django.shortcuts import render
from django.views.generic import TemplateView
from fusion.models import Services, Team_Members


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['employees'] = Team_Members.objects.order_by('?').all()

        return context
