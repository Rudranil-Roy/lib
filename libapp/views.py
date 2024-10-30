from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book, Reader
import datetime
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

def returnbook(request,pk):
    
    reader=Reader.objects.get(id=pk)
    book=reader.book_borrowed
    reader.book_borrowed=None
    book.book_count+=1
    book.save()
    reader.save()

    return redirect('reader','1')

def deleteuser(request,pk):
    
    reader=Reader.objects.get(id=pk)
    if reader.book_borrowed != None:
        book=reader.book_borrowed
        book.book_count+=1
        book.save()
    reader.delete()

    return redirect('reader','1')