from django.shortcuts import render
from django.http import JsonResponse
from datetime import date

import json

from api.models import Question

from api.serializers import QuestionSerializer

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


# Create your views here.
def search_answers(self, *args, **kwargs):

    content = {
        'question': 'question_body',
        'page': 'page_number'
    }
    return JsonResponse(content, status=status.HTTP_200_OK)



class QuestionView(ListCreateAPIView):
    def get(self, *args, **kwargs):
        question_body = self.kwargs.get('q')
        page_number = self.kwargs.get('page')
        # Question.objects.get_or_create(body=question_body)
        print(question_body)
        print(page_number)
        content = {
            'question': question_body,
            'page': page_number
        }
        return Response(content, status=status.HTTP_200_OK)






