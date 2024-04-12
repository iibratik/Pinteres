from django.shortcuts import render, get_object_or_404
from create.models import Photos

def index_main(request): 
    photos = Photos.objects.all() 
    return render(request, 'main/main.html', {'photos': photos})

def photo_detail(request, ps):
    photo = get_object_or_404(Photos, pk=ps)
    return render(request, 'main/photos.html', {'photo': photo})