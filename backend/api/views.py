from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("Welcome to Index View.")

def index(request):
    return HttpResponse("Welcome to API.")