from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Import Django authentication functions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Import built-in authentication forms


def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

'''def login(request):
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) #create form (built-in) with POST data (user fills in data)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Get the cleaned username
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) #authenticates the user
            if user is not None:
                login(request,user) #logs the user in
                return redirect()
            form.save()
            return redirect('') #if sign up is valid, user is redirected to login page
    else:
        form = UserCreationForm() #create blank form that is shown to the user (GET)
    return render(request, 'signup.html', {'form': form}) #render signup.html with the form'''

def signup(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) #create form (built-in) with POST data (user fills in data)
        if form.is_valid():
            form.save()
            return redirect('login') #if sign up is valid, user is redirected to login page
    else:
        form = UserCreationForm() #create blank form that is shown to the user (GET)
    return render(request, 'signup.html', {'form': form}) #render signup.html with the form
