from django import forms
from .models import feedback


# contact form
class feedbackForm(forms.ModelForm):  
    feedback_name = forms.CharField(widget=forms.TextInput(
        attrs={'name':'feedback_name',}), required=True, )
    feedback_email = forms.CharField(widget=forms.EmailInput(
        attrs={'name':'feedback_email',}), required=True,)
    feedback = forms.CharField(widget=forms.TextInput(
        attrs={'name':'feedback',}), required=True, )  
    
    class Meta:
        model = feedback
        fields = ['feedback_name', 'feedback_email', 'feedback', ]