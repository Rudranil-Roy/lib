from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'libapp/home.html',context={
        'Books':Book.objects.all()
    })