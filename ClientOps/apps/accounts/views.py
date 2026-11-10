from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
import structlog
from ..employee.models import Employee
# Create your views here.

logger = structlog.get_logger(__name__)
User = get_user_model()
def is_admin(user):
    return (user.is_authenticated and
            user.role== "Admin" )

def login_user(request):
    logger.info("Method: %s | GET: %s | POST: %s | URL: %s | User: %s",
                request.method,
                request.GET,
                request.POST,
                request.path,
                request.user.email)
    if request.user.is_authenticated :
        return redirect(to='/index')

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        email = request.POST.get("username")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user and user.blocked_user:
            messages.error(request, 'Your account is blocked.')

        elif form.is_valid() :
            user= form.get_user()
            user.number_login = 0
            user.save(update_fields=['number_login'])
            login(request, user)
            if user.first_login:
                return redirect('user:change_password')

            return redirect('/index')

        else:
            if user:
                user.number_login += 1

                if user.number_login >= 3:
                    user.blocked_user = True
                    user.save(update_fields=['blocked_user',"number_login"])
                    messages.error(request, 'Your account is blocked.')
                else:
                    user.save(update_fields= ["number_login"])
                    messages.error(request, 'Email or password did not match')
            else:
                messages.error(request, 'Email or password did not match')
    else:
        form = LoginForm()
    return render(request ,'user/login.html', context={'form':form})
@login_required
def logout_user(request):
    logger.info("Method: %s | GET: %s | POST: %s | URL: %s | User: %s",
                request.method,
                request.GET,
                request.POST,
                request.path,
                request.user.email)
    logout(request)
    return redirect('user:login')

@user_passes_test(is_admin)
def signupuser(request):
    logger.info("Method: %s | GET: %s | POST: %s | URL: %s | User: %s",
                request.method,
                request.GET,
                request.POST,
                request.path,
                request.user.email)
    if request.method == 'POST':

        form = RegistrationForm( data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user:register')
    else:
       form = RegistrationForm()
    return render(request ,'user/signup.html', context={'form':form})



@login_required
def change_password(request):
    logger.info("Method: %s | GET: %s | POST: %s | URL: %s | User: %s",
                request.method,
                request.GET,
                request.POST,
                request.path,
                request.user.email)
    if request.method == 'POST':
        form = ChangePasswordForm(user= request.user  ,data=request.POST)
        if form.is_valid():
            user = form.save()
            user.first_login = False
            user.save(update_fields=['first_login'])
            update_session_auth_hash( request, user )

            messages.success(request, 'Password changed successfully')
            return redirect('/index')
    else:
        form = ChangePasswordForm(user= request.user )
    return render(request, 'user/change_password.html', {"form":form})