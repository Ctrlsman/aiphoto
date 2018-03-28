from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    print(111)
    return HttpResponse('nihao')