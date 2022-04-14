from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_all),
    path('', views.index, name='index'),
]