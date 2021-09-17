from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import BlogModel
from .forms import BlogForm
# from django.http import HttpResponse
# Create your views here.
def HomeView(request):
    blog=BlogModel.objects.all()
    content={'blogs':blog}
    return render(request,'home.html',content)

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def aboutView(request):
    return render(request,'About.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def RegisterView(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('Username')
        email = request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        print(fname,lname,uname,email,pass1,pass2)
        if pass1!=pass2:
            messages.warning(request,'Passwords do not match')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exists')
            return redirect('register')
        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=pass1)
            user.save()
            messages.success(request,'User created successfully')
            return redirect('login')
    return render(request,'Register.html')

def AddBlogView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        blog=BlogModel(title=title, description=description,user_id=request.user)
        blog.save()
        messages.success(request,'post has been submitted successfully')
        return redirect('addblog')
    return render(request,'addblog.html')

def BlogDetailView(request,id):
    blog=BlogModel.objects.get(id=id)
    content={'blogkey':blog}
    return render(request,'blog_detail.html',content)

def DeleteView(request,id):
    blog=BlogModel.objects.get(id=id)
    blog.delete()
    messages.success(request,'blog has been deleted successfully')
    return redirect('home')

def EditView(request,id):
    blog=BlogModel.objects.get(id=id)
    edit=BlogForm(instance=blog)
    if request.method =="POST":
        form=BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"blog has been edited successfully")
            return redirect('home')
    return render(request,'edit_blog.html',{'key':edit})
