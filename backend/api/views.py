from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import database, benchmark_cypher, benchmark_sql


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")

def reset():
    res = database.reset()
    return JsonResponse(res)

def benchmark_deal():
    json_cypher = benchmark_cypher.get_deals()
    json_sql = benchmark_sql.get_deals()
    combined_json = {**json_cypher, **json_sql}
    return JsonResponse(combined_json)


@csrf_exempt
def command(request, action):
    if(action == 'reset'):
        return reset()
    elif(action == 'deal'):
        return benchmark_deal()
    return JsonResponse({"method": request.method})
