from django import forms
from .models import Free_Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Free_Book
        fields = ['book_cover', 'book_title', 'book_description', 'book_pdf']

