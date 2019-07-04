from django.contrib import messages
from django.views.generic import TemplateView


class CalcView(TemplateView):
    template_name = 'app/calc.html'
