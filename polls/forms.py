from django.forms import ModelForm
from django  import forms
from .models import Home


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    Categories = forms.ChoiceField( choices=[('question','Question'),('other','Other')])
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class HomeForm(ModelForm):
    """Form definition for Home."""

    class Meta:
        """Meta definition for Homeform."""

        model = Home
        fields = '__all__'






