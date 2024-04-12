from django.urls import path
from . import views 

app_name = 'main'

urlpatterns = [
    path('', views.index_main, name='main'),
    path('<int:ps>/', views.photo_detail, name='photo_detail')
]