from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Import Django authentication functions
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) #create form (built-in) with POST data (user fills in data)
        if form.is_valid():
            form.save()
            return redirect('login') #if sign up is valid, user is redirected to login page
    else:
        form = CustomUserCreationForm() #create blank form that is shown to the user (GET)
    return render(request, 'signup.html', {'form': form}) #render signup.html with the form
