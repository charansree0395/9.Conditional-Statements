from django.shortcuts import render

# Create your views here.

def conditional(request):
    d={'a':5}
    return render(request,'if block.html',d)

def condition(request):
    d1={'m':40,'n':60}
    return render(request,'if-else.html',d1)


def condi(request):
    d2={'a':100,'b':2000,'c':450}
    return render(request,'if-elif-else.html',d2)


def con(request):
    d3={'x':980,'y':900,'z':3000}
    return render(request,'Nested if.html',d3)