from django.urls import path
from . import views

urlpatterns = [
    path("", views.home ,name="homeURL"),
    path("add/", views.add , name="agregarURL"),
]
