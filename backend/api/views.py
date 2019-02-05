from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db import database

# Create your views here.
def index_view(request):
    return HttpResponse("Welcome to Index View.")

def index(request):
    return HttpResponse("Welcome to API.")

def insert(request):
    cypher_res = database.insert('cypher')
    return JsonResponse(cypher_res)