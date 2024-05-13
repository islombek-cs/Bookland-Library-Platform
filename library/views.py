from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse, reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# Create your views here.
def home(request):
    free_books = Free_Book.objects.all()[:3]

    context = {
        'free_books': free_books
    }

    return render(request, "library/home.html", context)

def about(request):
    return render(request, "library/about.html")

def blogs(request):
    return render(request, "library/blogs.html")

def blog_detail(request):
    return render(request, "library/blog_detail.html")

def purchase_book(request):
    return render(request, "library/purchase_book.html")

def free_books(request):
    if request.method == 'POST':
        form = Free_Book(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = Free_Book()

    free_books = Free_Book.objects.all()

    search_query = request.GET.get('q', '')
    print("Search Query:", search_query)  # Check what query is being received
    if search_query:
        books = Free_Book.objects.filter(book_title__icontains=search_query)
        print("Filtered Books:", books)  # Check the filtered queryset
    else:
        books = Free_Book.objects.all()

    free_books = books  # Simplified to use one variable

    context = {
        'books': books,
        'free_books': free_books
    }

    return render(request, "library/free_books.html", context)


def find_readers(request):
    return render(request, "library/find_readers.html") 

def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            return redirect('register')
    return render(request, 'library/register.html')

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'library/login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")


