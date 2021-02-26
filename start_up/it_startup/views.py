from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        msg = request.POST.get('msg')
        print(name, email, msg)
        return redirect('home')
    else:
        return render(request, 'it_startup/index.html')
