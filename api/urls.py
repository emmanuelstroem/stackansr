# api/urls.py

from django.urls import path, re_path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.PeopleView.as_view(lookup_field='body')),
    # path('search', views.QuestionView.as_view())
    re_path(r'^search$', views.search_answers, name="get_answers")
]