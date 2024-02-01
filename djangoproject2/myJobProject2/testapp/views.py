from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def display1(request):

    return HttpResponse("<h2>How are you doing?</h2>")

def display2(request):
    return HttpResponse('<h2>The second view</h2>')

def display3(request):
    return HttpResponse('<h2>The third view</h2>')

def display4(request):
    return HttpResponse('<h2>The fourth view</h2>')

def display5(request):
    return HttpResponse('<h2>The fivety view</h2>')

def wish(request):
    return render(request,'testapp/wish.html')