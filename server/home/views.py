from django.shortcuts import render

class TemplateHome():
    def Home(request):
        return render(request, 'Home.html')
