from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def recommend(request):
    return render(request,'recommend.html')

def subscribe(request):
    return render(request,'subscribe.html')

def shopping(request):
    return render(request,'shopping.html')

def payment(request):
    return render(request,'payment.html')
def result(request):
    return render(request,'result.html')

def mypage(request):
    return render(request,'mypage.html')
