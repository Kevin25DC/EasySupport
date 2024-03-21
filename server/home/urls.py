from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.Home, name="home"),  
    path('login/', views.loginOrRegister.login_view, name='login'), 
    path('Register/', views.loginOrRegister.Register, name='Register'), 
    path('Desk',views.HelpDesk.Heldesk,name='HelpDesk'), 
]
