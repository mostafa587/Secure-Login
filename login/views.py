from django.shortcuts import render
from django.http import HttpResponse
from signup.models import User

# Create your views here.


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return render(request, 'login/login.html', {'error': 'All fields are required'})
        if not User.objects.filter(username=username).exists():
            return render(request, 'login/login.html', {'error': 'Username does not exist'})
        elif not User.objects.filter(password=password).exists():
            return render(request, 'login/login.html', {'error': 'Password is incorrect'})
        else:
            return HttpResponse('Login successful')
    return render(request, 'login/login.html')

