from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    
    path('purchase_book/', views.purchase_book, name='purchase_book'),
    path('free_books/', views.free_books, name='free_books'),
    path('find_readers/', views.find_readers, name='find_readers'),
    
]