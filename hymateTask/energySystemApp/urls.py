from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("generate_simulation", views.generate_simulation, name="generate_simulation"),s
]