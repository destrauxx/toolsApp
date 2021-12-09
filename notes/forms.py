
from django import forms

from .models import Note, Collection

class CreateNoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'header',
            'text',
        ]

class CreateCollectionModelForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            'name',
            
        ]
