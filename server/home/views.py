from django.shortcuts import render
from .models import User

def Home(request):
    return render(request,'Home.html')

class loginOrRegister():
    def login_view(request):
        if request.method == 'POST':
            user = request.POST.get('user',None)
            password = request.POST.get('password',None)
            if user:
                user = User.objects.get(Username=user,password =password)

        return render(request,'Login.html')
    
    def Register(request):
        pass

