from django import forms
from django.forms import ModelForm, Textarea
from .models import Contact, Documentfile
from .validators import validate_email_guest

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(
            required = True,
            label ="Name",
            widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'mb-3'})
        )
    
    
    email = forms.EmailField(
        required = True,
        label ="Email",
        widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'mb-3'}),
        validators=[validate_email_guest]
    )
    
    
    subject = forms.CharField(
        required = True,
        label ="Subject",
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'mb-3'})
    )
    
    message = forms.CharField(
        required = True,
        label ="Message", 
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
    
    class Meta:
        model = Contact
        fields = '__all__'


class DocumentfileForm(forms.ModelForm):
    doc_file = forms.TimeField(
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Choose Your File', 'type':'file', 'class': 'form-control fileinput form-control-file bg-second mb-3'}),
    )

    email = forms.EmailField(
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email', 'type': 'email', 'class': 'form-control bg-second mb-3'}),
        validators=[validate_email_guest]
    )

    class Meta:
        model = Documentfile
        fields = '__all__'
        
        