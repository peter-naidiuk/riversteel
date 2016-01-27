from django.conf.urls import url, include
from django.contrib import admin
from .views import MainPageView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main_page'),
]
