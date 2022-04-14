from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list),
    path('', views.index, name='index'),
]