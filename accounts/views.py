from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from accounts.models import User
from accounts.forms import AuthenticationForm, RegistrationForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request,user)
                    request.session['username'] = user.username
                    return redirect('/accounts/loggedin')
            else:
                return redirect('/accounts/invalid_loggedin')
    else:
        try:
            user = User.objects.get(username=request.session['username'])
            if user is not None:
                if user.is_active:
                    #django_login(request,user)
                    return redirect('/accounts/loggedin')
        except KeyError:
            pass
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form': form,})

def loggedin(request):
    return render(request,'accounts/loggedin.html',{'user':request.user})

def invalid_login(request):
    return render(request,'accounts/invalid_login.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/register_success')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html', {'form':form,})

def register_success(request):
    return render(request,'accounts/register_success.html')

def logout(request):
    django_logout(request)
    try:
        del request.session['username']
        del request.session['password']
    except KeyError:
        pass
    return render(request,'accounts/logout.html')
