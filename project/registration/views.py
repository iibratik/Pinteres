from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def index_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['User_Name']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email']
            
            if Registration.objects.filter(User_Name=username).exists() or \
               Registration.objects.filter(Email=email).exists():
                return render(request, 'main/registration.html', {'form': form, 'error_message': 'Username or email already exists'})
            
            registration = Registration(User_Name=username, Password=password, Email=email)
            registration.save()
            
            return redirect('main:main')
    else:
        form = RegistrationForm()
    
    return render(request, 'main/registration.html', {'form': form})