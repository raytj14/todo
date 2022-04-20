from django.urls import path

from . import views

urlpatterns = [
    path("CBV", views.CBView.as_view())
]