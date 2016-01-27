from django.conf.urls import url, include
from django.contrib import admin
from .views import MetalProductsView, MetalProductsMainView

urlpatterns = [
    url(r'^$', MetalProductsMainView.as_view(), name='metal_products_main_page'),
    url(r'^(?P<page_name>[a-z]+)', MetalProductsView.as_view(), name='metal_products_page')
]
