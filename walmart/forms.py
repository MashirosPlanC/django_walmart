from django import forms

class SignInForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class MyForm(forms.Form):
    name = forms.CharField(max_length = 100)
    age = forms.IntegerField()
    email = forms.EmailField()