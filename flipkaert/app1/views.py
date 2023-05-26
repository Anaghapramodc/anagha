from django.http import HttpResponse
from django.shortcuts import render
from .models import product


# Create your views here.
def index(request):
    return HttpResponse("hai dear")


def test_fun(request):
    return render(request, 'test.html')
