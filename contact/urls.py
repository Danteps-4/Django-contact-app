from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path("view/", views.view, name="view"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("create/", views.create, name="create"),
]