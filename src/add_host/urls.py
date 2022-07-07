from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sign_up/', views.RegisterFormView.as_view()),
    path('login_user/', views.LoginFormView.as_view()),
    path('list_host/', views.host_list)
]
