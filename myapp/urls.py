from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('',HomeView,name='home'),
   path('login',LoginView,name='login'),
   path('register',RegisterView,name='register'),
   path('about',aboutView,name='about'),
   path('logout',logoutView,name='logout'),
   path('addblog',AddBlogView,name='addblog'),
   path('blog_detail/<int:id>',BlogDetailView,name='blog_detail'),
   path('edit/<int:id>',EditView,name='edit'),
   path('delete/<int:id>',DeleteView,name='delete'),
]