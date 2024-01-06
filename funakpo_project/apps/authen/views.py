from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignForm

# Create your views here.

def SignUp(request):
    form=SignForm()
    if request.method=="POST":
        form=SignForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you have successfully signed up')
            return redirect('home')

    return render(request, 'authen/signup.html', {'form':form})

def SignIn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you are welcome')
            return redirect('home')
        
        else:
            return render(request, 'authen/signin.html')
    return render(request, 'authen/signin.html')

def Logout(request):
    logout(request)
    return redirect('home')

