from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':100}
    return render(request,'conditions.html',context=d)
def conditions(request):
    d={'a':20,'b':30}
    return render(request,'conditions.html',context=d)
def conditions(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'conditions.html',context=d)
def conditions(request):
    d={'a':20,'b':30,'c':40,'d':50}
    return render(request,'conditions.html',context=d)
def loop(request):
    d={'name':'mahendhra'}
    return render(request,'loop.html',context=d)