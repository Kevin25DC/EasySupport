from django.shortcuts import render

def Home(request):
    return render(request,'Home.html')

def login_view(request):
    return render(request,'Login.html')