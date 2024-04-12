from django.shortcuts import render, get_object_or_404
from registration.models import Registration

def account_detail(request, acc):
    account = get_object_or_404(Registration, id=acc)
    return render(request, 'main/account.html', {'account': account})