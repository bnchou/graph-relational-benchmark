from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .db import database, benchmark_cypher, benchmark_sql


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")


@csrf_exempt
def command(request, action):
    if(action == 'reset'):
        return JsonResponse(database.reset())
    elif(action == 'amount'):
        if(request.body):
            database.save_amount_to_file(request.body.decode('utf-8'))
        return JsonResponse({"amount": database.get_amount_from_file()})

    print('\nBenchmarking Neo4j...')
    cypher = benchmark_cypher.run(action)
    print('\nBenchmarking MS SQL...')
    sql = benchmark_sql.run(action)
    return JsonResponse({
        'cypher': cypher,
        'sql': sql
    })


@csrf_exempt
def commands(request):
    return JsonResponse({
        'cypher': benchmark_cypher.raw_queries,
        'sql': benchmark_sql.raw_queries
    })
