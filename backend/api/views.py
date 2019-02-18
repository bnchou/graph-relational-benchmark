from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import database


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")


def reset():
    res = database.reset()
    return JsonResponse(res)


@csrf_exempt
def command(request, action):
    if(action == 'reset'):
        return reset()
    print(action)
    return JsonResponse({"method": request.method})
