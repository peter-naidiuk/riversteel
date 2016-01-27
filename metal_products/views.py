import os
from django.shortcuts import render
from django.views.generic import TemplateView

class MetalProductsView(TemplateView):

    def get_template_name(self, **kwargs):
        return os.path.join('metal_products', self.kwargs['page_name']) + '.html'

class MetalProductsMainView(TemplateView):
    template_name = 'metal_products/home_table.html'
# Create your views here.
