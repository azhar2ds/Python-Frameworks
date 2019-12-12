from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunc(request):
    return HttpResponse('Welcome the first app')
def myfunc2(request):
    return HttpResponse('This is the second page')
def myfunc3(request):
    return HttpResponse('This is third page ')
def myfunc4(request):
    return HttpResponse('This is fourth page ')
def myfunc5(request):
    return HttpResponse('This is fifth page')
    return HttpResponse('<html><body bgcolor=blue><h1>This is fifth page</h1></body><html> ')

# azhar2ds@gmail.com
# 2015