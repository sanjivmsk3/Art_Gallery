from django import forms
from gallery.models import Item

class Insert(forms.ModelForm):
    class Meta:
        model = Item 
        fields = '__all__'