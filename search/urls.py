# search/urls.py

from django.urls import path, re_path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.index, name='index'),
    path('?q=<str:question>', views.search, name='search'),
     re_path(r'^$', views.search, name='search'),
]