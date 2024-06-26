from django.forms import ModelForm, TextInput, FileInput
from .models import Photos

class PhotosForm(ModelForm):
    class Meta:
        model = Photos
        fields = ['Name', 'Description', 'Photo', 'Tags']
        widgets = {
            'Имя': TextInput(),
            'Description': TextInput(),
            'Photo': FileInput(),
            'Tags': TextInput(),
        }