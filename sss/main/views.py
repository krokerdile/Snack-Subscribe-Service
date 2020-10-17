from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def recommend(request):
    return render(request,'recommend.html')

def subscribe(request):
    return render(request,'subscribe.html')

def shopping(request):
    return render(request,'shopping.html')


    
