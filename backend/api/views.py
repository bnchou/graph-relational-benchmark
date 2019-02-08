from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db import database


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")


def cypher_reset(request):
    res = database.reset('cypher')
    return JsonResponse(res)


def sql_reset(request):
    res = database.reset('sql')
    return JsonResponse(res)
