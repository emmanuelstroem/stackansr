from django.shortcuts import render
from django.http import HttpRequest

import requests, json, os

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from . import helpers
from api.Helpers import get_answers

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search(request, *args, **kwargs):
    question = request.GET.get('q')
    page = request.GET.get('page')

    params = {
            'question': question,
            'page': page
        }

    url = "http://"+request.get_host()+"/api/search"

    local_json_data = read_local_file('/search/answers.json')

    # response = requests.get(url, params)

    # answers = get_answers(question, page)

    # print(local_json_data["items"][0])

    content = {
        'question': question
    }
    # return Response(answers.content)
    return render(request, 'search/test.html', {'questions': local_json_data["items"]} )
    # return Response(content, template_name='search/results.html')

def read_local_file(file_name):

    file_path = os.path.dirname(os.path.dirname(__file__)) + file_name
    with open(file_path, 'r') as json_file:
    # my_json_obj = json.load(f)
    # open_file = open(file_name)
        loaded_data = json.load(json_file) # deserialises it
        dumped_data = json.dumps(loaded_data) # json formatted string

    # open_file.close()

        return loaded_data