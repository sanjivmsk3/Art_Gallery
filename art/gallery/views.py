from django.shortcuts import render,redirect
from gallery.models import Item
from .forms import *

# Create your views here.
def home(request):
    data = {
        'item':Item.objects.all(),
    }
    return render(request,'home.html',data)

def insert(request):
    form = Insert (request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'insert.html',{
        'inserts':form,
        })
