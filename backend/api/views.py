from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db import database


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")


def cypher_insert(request):
    res = database.insert('cypher')
    return JsonResponse(res)


def sql_insert(request):
    res = database.insert('sql')
    return JsonResponse(res)
