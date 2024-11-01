from django import forms
from .models import *

class Bookform(forms.ModelForm):
    
    class Meta:
        model=Book
        fields=['book_name', 'author_name', 'book_img', 'isbn_number', 'book_count']

class Readerform(forms.ModelForm):

    class Meta:
        model=Reader
        exclude=['book_borrowed', 'date_borrowed', 'return_date', 'created_at', 'active']