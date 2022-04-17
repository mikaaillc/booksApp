from django.shortcuts import render ,HttpResponse

def register_view(request):

    return render(request,'users.html')

def login_view(request):

    return render(request,'login.html')

def home_view(request):

    return render(request,'home.html')