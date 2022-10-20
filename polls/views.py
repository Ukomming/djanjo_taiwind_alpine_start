from pyexpat import model
from this import d
from unicodedata import name
from django.shortcuts import render
from .models import Home
from .forms import HomeForm
from .forms import ContactForm

# Create your views here.
def home(request):
    homes = Home.objects.all()
    context ={'homes':homes}
    return render(request, 'home.html',context)

def ModelForm(request):
    form = HomeForm()
    context={"form":form}
    return render(request, 'Modelform.html', context)

def Form(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            email =form.cleaned_data['email']
            print(name, email)
    form = ContactForm()
    context={"form":form}
    return render(request, 'form.html', context)