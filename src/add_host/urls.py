from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_host/sign_up/', views.RegisterFormView.as_view()),
    path('add_host/login_user/', views.LoginFormView.as_view()),
]
