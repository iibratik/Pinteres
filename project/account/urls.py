from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('<int:acc>/', views.account_detail, name='account_detail'),
]