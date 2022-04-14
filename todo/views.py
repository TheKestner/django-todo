from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Todo, Event, Category
from .serializers import TodoSerializer, EventSerializer, CategorySerializer

# Create your views here.

def index(request):
    return HttpResponse("HELLO WORLD")

def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)