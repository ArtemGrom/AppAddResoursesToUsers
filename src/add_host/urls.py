from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_host/sign_up/', views.sign_up, name="sign-up"),
]