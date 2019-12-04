from django.shortcuts import render
from django.http import JsonResponse
from datetime import date

import os, json, requests

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
filter_string = '!)5cCAwGtBu-iwGhY-LIHRXHqmZLe'
default_page_size = 20

def get_questions(question_body, page=1, qns_per_page=default_page_size):
    url = build_request_url(question_body, page, qns_per_page)
    # print(url)
    headers = build_request_headers()
    response = requests.get(url, headers=headers)
    return response

def get_questions_for(question_body, page=1, qns_per_page=default_page_size):
    url = build_request_url(question_body, page, qns_per_page)
    # print(url)
    headers = build_request_headers()
    response = requests.get(url, headers=headers)
    return response


def build_request_url(question_body, page, qns_per_page):
    request_body = build_request_body(body=question_body, page_number=page, page_size=qns_per_page)
    # print(request_body)
    url = base_url + request_body
    return url

def build_request_body(body, page_number, site='stackoverflow', accepted=True, sort_by='activity', order_by='desc', page_size=default_page_size):
    question_url = build_question_url(body, page_number, page_size, accepted)
    filters = build_filters(sort_by, order_by, site)
    request_body = "/search/advanced?" + question_url + filters
    # print (request_body)
    return request_body

def build_question_url(body, page_number, page_size, accepted):
    question_url = "q={0}&page={1}&pagesize={2}&accepted={3}".format(body, page_number, page_size, str(accepted))
    return question_url

def build_filters(sort_by, order_by, site):
    filters = "&sort={0}&order={1}&site={2}&key={3}&filter={4}".format(sort_by, order_by, site, api_key, filter_string)
    return filters

def build_default_params():
    params = {
        'site': 'stackoverflow',
        'sort': 'activity'
    }
    return params

def build_request_headers():
    headers = {
        "content-type": "application/json; charset=utf-8",
        "allow_redirects": "False",
        "Access-Control-Allow-Credentials": "False",
        "Access-Control-Allow-Origin": "*",
        "X-Content-Type-Options": "nosniff",
        "Content-Encoding": "gzip"
    }
    return headers


