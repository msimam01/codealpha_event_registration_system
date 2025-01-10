from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
        first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    
    old_password = forms.CharField(label="Current Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Current Password'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Confirm New Password'}))
    
        