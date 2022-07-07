from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sign_up/', views.RegisterFormView.as_view()),
    path('login_user/', views.LoginFormView.as_view()),
    path('list_host/', views.HostListView.as_view(), name='list_host'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.HostUpdateView.as_view()),
]
