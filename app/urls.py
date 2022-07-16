from django.urls import path
from . import views

# Create your patterns here
urlpatterns = [
    path("", views.login_view, name="login"),
    path("index/", views.index_view, name="index"),
    path("create/", views.create_view, name="create"),
    path("logout/", views.logout_view, name="logout"),
    path("edit/<str:pk>/", views.edit_view, name="edit"),
    path("register/", views.register_view, name="register"),
    path("delete/<str:pk>/", views.delete_view, name="delete"),
]
