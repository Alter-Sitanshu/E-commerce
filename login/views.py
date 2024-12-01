from django.shortcuts import render,redirect
from .models import Account
from home.models import Cart
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['again_password']:
            form = RegisterForm()
            return render(request, "login/register.html", context={
                "form":form,
                "warning":"Passwords did not match !"
            })
        elif User.objects.filter(email = data['email']).count() > 0:
            form = RegisterForm()
            return render(request, "login/register.html", context={
                "form":form,
                "warning":"Email already in user. Login"
            })
        else:
            try:
                new_user = User.objects.create_user(
                    username=data['name'],
                    email=data['email']
                )
                new_user.set_password(data['password'])
                new_user.save()
            except:
                form = RegisterForm()
                return render(request, "login/register.html", context={
                    "form":form,
                    "warning":"Username Taken"
                })
            else:
                new_account = Account.objects.create(
                    user = new_user,
                    type = data['type']
                )
                new_account.save()
                cart = Cart.objects.create( account = new_account )
                cart.save()
                return redirect('login')

    return render(request, "login/register.html", context={"form":form})
    
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['name']
        password = form.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            return render(request, "login/register.html", context={
                    "form": form,
                    "warning": "User does not exist"
                })
        user = authenticate(username = username, password = password)
        if user == None:
            return render(request, "login/register.html", context={
                    "form": form,
                    "warning": "Passwords do not match. Please try again."
                })
        else:
            login(request, user)
            return redirect('landing:index')
    return render(request, 'login/register.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing:index')