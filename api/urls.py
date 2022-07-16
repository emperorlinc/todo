from django.urls import path
from . import views

# Create your patterns here.
urlpatterns = [
	path("", views.apiOverview, name="api-overview"),
	path("todo-list/", views.todo_list, name="todo-list"),
	path("todo-create/", views.todo_create, name="todo-create"),
	path("todo-detail/<str:pk>/", views.todo_detail, name="todo-detail"),
	path("todo-update/<str:pk>/", views.todo_update, name="todo-update"),
	path("todo-delete/<str:pk>/", views.todo_delete, name="todo-delete"),
]
