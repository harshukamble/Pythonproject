from django.shortcuts import render,HttpResponseRedirect
from .forms import signupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.shortcuts import render



def logout_view(request):
        return render(request,'accounts/index.html')
#signup
from django.shortcuts import render, redirect
def register_view(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! You have successfully registered.')
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = signupForm()
    return render(request, 'accounts/register.html', {'form': form})
#login
def login_view(request):
        if request.method=='POST': 
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/user/')
        else:
            form=LoginForm()
        return render(request,'accounts/signin.html',{'form':form})
def index(request):
    return render (request,'accounts/index.html') 
def assist(request):
    return render (request,'accounts/assist.html')
def search(request):
    return render (request,'accounts/search.html')


def user(request):

    if request.user.is_authenticated:
        user=request.user
        name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'accounts/user.html',{"name":name,"gp":gps})
    else:
        return HttpResponseRedirect('/accounts/login/')
    
