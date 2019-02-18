from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import database, benchmark_sql as bs, benchmark_cypher as bc


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")

def reset():
    res = database.reset()
    return JsonResponse(res)

def benchmark(cypher, sql):
    json_cypher = cypher
    json_sql = sql
    combined_json = {**json_cypher, **json_sql}
    return JsonResponse(combined_json)


@csrf_exempt
def command(request, action):
    if(action == 'reset'):
        return reset()
    elif(action == 'deal'):
        return benchmark(bc.get_deals(), bs.get_deals())
    elif(action == 'history'):
        return benchmark(bc.get_history(), bs.get_history())
    elif(action == 'persons'):
        return benchmark(bc.get_persons(), bs.get_persons())
    elif(action == 'update_deals'):
        return benchmark(bc.update_deals(), bs.update_deals())
    elif(action == 'update_companies'):
        return benchmark(bc.update_comp_names(), bs.update_comp_names())
    return JsonResponse({"method": request.method})
