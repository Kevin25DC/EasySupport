from django.shortcuts import render,redirect
from .models import User
from .forms import registerUser
import random

def Home(request):
    return render(request,'Home.html')

class loginOrRegister():
    def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(Username=username, Password=password)
               
                return redirect('HelpDesk')  
            except User.DoesNotExist:
                pass
        return render(request, 'Login.html') 
    
    def Register(request):
        if request.method == 'POST':
            form = registerUser(request.POST)
            if form.is_valid():
                email = form.cleaned_data['Email']
                if User.objects.filter(Email=email).exists():
                    return render(request,'Register.html',{'form':form,'user_exists':True})   
                else:
                    form.save()
                    return redirect('login')
            else:
                return render(request,'Register.html',{'form':form,'invalid_form':True})
        else:
            form = registerUser()

        return render(request,'Register.html',{'form':form})    
    
class HelpDesk():
    def Heldesk(request):
        return render(request,'portalHelp.html')        

