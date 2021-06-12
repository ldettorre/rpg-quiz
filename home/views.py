from django.shortcuts import render

# Create your views here.

def index(request):
    request.session.clear() 
    return render(request, 'home/index.html')

def faq(request):
    request.session.clear()
    return render(request, 'home/faq.html')