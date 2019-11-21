# search/helpers.py

import os, requests

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class Helpers():
    api_key = os.getenv('API_KEY')

    def get_answers_for(self, question, page):
        params = {
            'question': question,
            'page': page
        }
        response = requests.get('/api/search', params)

        return response