from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.db.models import Q
from .models import Book, Reader
import datetime
# Create your views here.

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    books=Book.objects.filter(
        Q(book_name__icontains=q) |
        Q(author_name__icontains=q) |
        Q(isbn_number__icontains=q)
    )
    return render(request,'libapp/home1.html',context={
        'Books':books
    })

@login_required(login_url='login')
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

    return render(request,'libapp/addreader.html')

@login_required(login_url='login')
def reader(request,pk):

    if request.method=='POST':
        isbn=int(request.POST.get('no'))
        print(isbn)
        book=Book.objects.get(isbn_number=isbn)
        reader=Reader.objects.get(id=pk)

        if(book.book_count>0):
            reader.book_borrowed=book
            book.book_count-=1
            date=datetime.date.today()
            reader.date_borrowed=date
            returndate= date+ datetime.timedelta(days=7)
            reader.return_date=returndate
            book.save()
            reader.save()
            return redirect('reader',"1")
        else:
            return HttpResponse('Book Out of Stock')



    return render(request,'libapp/reader.html',context={
        'Readers':Reader.objects.all()
    })

@login_required(login_url='login')
def addbook(request):
    if request.method=='POST':
        book_name=request.POST.get('name')
        isbn=int(request.POST.get('no'))
        author_name=request.POST.get('author')
        count=int(request.POST.get('count'))
        print(book_name,isbn,author_name,count)

        book=Book(book_name=book_name,author_name=author_name,isbn_number=isbn,book_count=count)
        book.save()
        return redirect('addbook')

    return render(request,'libapp/addbook.html')

@login_required(login_url='login')
def returnbook(request,pk):
    
    reader=Reader.objects.get(id=pk)
    book=reader.book_borrowed
    reader.book_borrowed=None
    book.book_count+=1
    book.save()
    reader.save()

    return redirect('reader','1')

@login_required(login_url='login')
def deleteuser(request,pk):
    
    reader=Reader.objects.get(id=pk)
    if reader.book_borrowed != None:
        book=reader.book_borrowed
        book.book_count+=1
        book.save()
    reader.delete()

    return redirect('reader','1')

@login_required(login_url='login')
def updatebook(request,pk):
    book=Book.objects.get(id=pk)
    book.book_count+=int(request.POST.get('no'))
    book.save()
    return redirect('home')

@login_required(login_url='login')
def deletebook(request,pk):
    book=Book.objects.filter(id=pk)
    book.delete()
    return redirect('home')

def loginp(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'libapp/login.html')

@login_required(login_url='login')
def logoutp(request):
    logout(request)
    return redirect('home')