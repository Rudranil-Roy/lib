from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)
    isbn_number=models.IntegerField()
    book_count=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name



class Reader(models.Model):
    reader_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact_no=models.IntegerField()
    address=models.TextField()
    active=models.BooleanField(default=True)
    book_borrowed=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    date_borrowed=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reader_name


class Librarian(models.Model):
    lib_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact_no=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return self.lib_name

