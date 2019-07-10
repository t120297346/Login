from django.shortcuts import render
from django.shortcuts import redirect
from . import models
# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "All forms are required"
        if (username and password):
            username = username.strip() #去除左右空格
            try:
                user = models.User.objects.get(name = username)
            except:
                message = "No this user"
                return render(request, 'login/login.html', {'message': message})
            if password == user.password:
                message = "wrong password"
                return redirect('/index/')
            else:
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')

def register(request):
    pass
    return render(request, 'login/register.html')

def logout(request):
    pass
    return redirect('/index/')