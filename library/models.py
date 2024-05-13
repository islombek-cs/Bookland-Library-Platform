from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Free_Book(models.Model):
    book_cover = models.ImageField(upload_to='books/covers/')
    book_title = models.CharField(max_length=255)
    book_description = models.TextField()
    book_pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.book_title
