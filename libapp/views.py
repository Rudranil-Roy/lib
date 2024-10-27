from django.shortcuts import render,redirect
from .models import Book, Reader
# Create your views here.

def home(request):
    return render(request,'libapp/home1.html',context={
        'Books':Book.objects.all()
    })

def addreader(request):

    if request.method=='POST':
        reader_id=request.POST.get('id')
        reader_name=request.POST.get('name')
        reader_email=request.POST.get('email')
        reader_no=int(request.POST.get('no'))
        reader_address=request.POST.get('address')

        reader= Reader(reader_id=reader_id,reader_name=reader_name,email=reader_email,contact_no=reader_no,address=reader_address)
        reader.save()

        return redirect('addreader')

    return render(request,'libapp/login.html')