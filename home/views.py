from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def faq(request):
    return render(request, 'home/faq.html')