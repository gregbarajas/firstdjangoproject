from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="name"),
    path("create/", views.create, name="create"),
    path("register/", views.create, name="create"),
]