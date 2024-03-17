from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.Home, name="home"),
    path('login/', views.login_view, name='login'),
]