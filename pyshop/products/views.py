import imp
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
    # return render(request,'base.html',{'products':products})
    # return HttpResponse("hello from httpresponse")



def testnewResponse(request):
    return HttpResponse("HTTPRESPONSE you have into url products/testnew/")