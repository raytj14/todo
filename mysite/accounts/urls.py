from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.HelloView.as_view() ),
    path('signup/', views.SignupView.as_view(), name='signup'), 
]