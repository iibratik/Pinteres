from django.shortcuts import render, redirect
from registration.models import Registration
from .forms import RegistrationForm

def index_login(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['User_Name']
            password = form.cleaned_data['Password']
            try:
                registration = Registration.objects.get(User_Name=user_name, Password=password)
                request.session['user_id'] = registration.id
                return redirect('account:account_detail', acc=registration.id)
            except Registration.DoesNotExist:
                error_message = 'Invalid username or password'
    else:
        form = RegistrationForm()
        error_message = None

    return render(request, 'main/login.html', {'form': form, 'error_message': error_message})