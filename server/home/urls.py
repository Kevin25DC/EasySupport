from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.TemplateHome.Home, name="home"),
]