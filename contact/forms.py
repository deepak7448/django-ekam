from django import forms
from .models import contact


class contactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form','name':'name','placeholder': 'Name...','id':"validationFullname",'type':"text",}), required=True, )
    phone = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control form','name':'phone', 'placeholder': 'Phone No...','id':"validationphone",'type':"number",}), required=True,)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control form','name':'email', 'placeholder': 'E-mail...','id':"validationEmail",'type':"email",}), required=True,)
    subjects = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control form','name':'subject','placeholder': 'Subject...','id':"validationSubject",'type':"text",}), required=True, )
    messages = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control form','name':'message', 'placeholder': 'Message...','id':"validationMessage",'type':"text",}), required=True,)    

    class Meta:
        model = contact
        fields = ['name','phone','email', 'subjects', 'messages',]


       
