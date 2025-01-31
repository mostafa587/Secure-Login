from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST['phone']
        return render(request, 'signup/signup.html')
    return render(request, 'signup/signup.html')
