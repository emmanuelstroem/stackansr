from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests, json, os

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from . import helpers
from api.Helpers import get_questions

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search(request, *args, **kwargs):
    question = request.GET.get('q')
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 20)
    next_page = int(page) + 1
    previous_page = int(page) - 1

    # url = "http://"+request.get_host()+"/api/search"
    # local_json_data = read_local_file('/search/answers.json')
    questions = get_questions(question, page, page_size).json()

    pages = {
        'current': page,
        'next': next_page,
        'previous': previous_page,
        'question': question,
        'range': range(1, int(questions['total']/20)),
        'total': questions['total']/20

    }

    return render(request, 'search/results.html', {'questions': questions['items'], 'has_more': questions['has_more'], 'total': questions['total'], 'pages': pages})

def read_local_file(file_name):
    file_path = os.path.dirname(os.path.dirname(__file__)) + file_name
    with open(file_path, 'r') as json_file:
        loaded_data = json.load(json_file) # deserialises it
        dumped_data = json.dumps(loaded_data) # json formatted string
        return loaded_data