from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .db import database, benchmark_cypher, benchmark_sql


def index_view(request):
    return HttpResponse("Welcome to Index View.")


def index(request):
    return HttpResponse("Welcome to API.")


def command(request, action):
    if(action == 'reset'):
        return JsonResponse(database.reset())
    return JsonResponse({
        'cypher': benchmark_cypher.run(action),
        'sql': benchmark_sql.run(action)
    })
