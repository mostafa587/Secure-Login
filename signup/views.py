from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email') # Returns <None> if "phone" is missing in the html form
        phone = request.POST['phone'] # Raises KeyError if "phone" is missing in the html form
        if not username or not password or not email or not phone: #could if username == None or password == None or email == None or phone == None:
            return render(request, 'signup/signup.html', {'error': 'All fields are required'})
    return render(request, 'signup/signup.html')
