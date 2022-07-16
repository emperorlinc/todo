from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
	api_urls = {
		"List": "/todo-list/",
		"Detail View": "todo-detail/<str:pk>/",
		"Create": "/todo-create/",
		"Update": "/todo-update/<str:pk>/",
		"Delete": "/todo-delete/<str:pk>/",
	}
	return Response(api_urls)

@api_view(["GET"])
def todo_list(request):
	todo = Todo.objects.all()
	serializer = TodoSerializer(todo, many=True)
	return Response(serializer.data)

@api_view(["GET"])
def todo_detail(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(todo, many=False)
	return Response(serializer.data)

@api_view(["POST"])
def todo_create(request):
	serializer = TodoSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(["POST"])
def todo_update(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=todo, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(["DELETE"])
def todo_delete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	return Response("Todo was successfully deleted")
