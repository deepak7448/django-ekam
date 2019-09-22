from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,PasswordResetForm


class signupForm(forms.Form):
    first_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form', 'placeholder': 'First Name','type':'text'}), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form', 'placeholder': 'Last Name','type':'text'}), required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form', 'placeholder': 'Username','type':'text'}), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class': 'form-control form', 'placeholder': 'Email address','type':'email'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form', 'placeholder': 'Create password','type':'password'}), required=True, max_length=50)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control form', 'placeholder': 'Confirm password','type':'password'}), required=True, max_length=50)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        a = User.objects.filter(username=username)
        if a.exists():
            raise forms.ValidationError("Username already exist")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        a = User.objects.filter(email=email)
        if a.exists():
            raise forms.ValidationError("Email already exist")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        MIN_LENGTH = 8
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password does't match")
            else:
                if len(password) < MIN_LENGTH:
                    raise forms.ValidationError(
                        "Password should have atleast %d characters" % MIN_LENGTH)
                if password.isdigit():
                    raise forms.ValidationError(
                        "Password should not all numeric")
                #first_isalpha = password[0].isalpha()
                #if all(c.isalpha() == first_isalpha for c in password):
                 #   raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        #" punctuation character.")
                #return password
                if not any(char.isdigit() for char in password):
                    raise forms.ValidationError('Password must contain at least One digit.')
                if not any(char.isalpha() for char in password):
                    raise forms.ValidationError('Password must contain at least One letter.')
                if not any(char.isupper() for char in password):
                    raise forms.ValidationError('Password must contain at least One Captial letter.')                
                if not any(char in "[!@#$%^&*()-_=+\|]}[{;:/?.>,<]" for char in password):
                    raise forms.ValidationError('Password must contain at least one special character.')
            
    class Meta():
        model = User
        fields = ['username', 'first_name','last_name','email', 'password']

class EditprofileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified E-Mail address.")
        return email


      