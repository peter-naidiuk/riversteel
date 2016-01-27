from django.shortcuts import render
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'company_details/main_page.html'

# Create your views here.
