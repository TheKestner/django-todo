from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Todo, Event, Category
from .serializers import TodoSerializer, EventSerializer, CategorySerializer

# Create your views here.

def index(request):
    return HttpResponse("HELLO WORLD")